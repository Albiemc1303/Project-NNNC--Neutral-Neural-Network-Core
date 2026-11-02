"""Step 10: hardened effect protocol atop Step 9 governance.
Atomic logical transitions only; no durable I/O, network, or concurrency guarantee.
"""
from dataclasses import dataclass, replace
from typing import Optional
from step9 import State, Command, apply

@dataclass(frozen=True)
class Effect:
    rid: str
    owner: str
    generation: int
    payload: str
    phase: str = 'PREPARED'  # PREPARED, COMMITTED, ACKED, ABORTED

@dataclass(frozen=True)
class Composite:
    base: State = State()
    effects: tuple[Effect,...] = ()
    def valid(self):
        if not self.base.valid(): return False
        if len({e.rid for e in self.effects})!=len(self.effects):return False
        for e in self.effects:
            r=next((r for r in self.base.ledger.reservations if r.rid==e.rid),None)
            if r is None or e.phase not in {'PREPARED','COMMITTED','ACKED','ABORTED'}:return False
            if e.phase=='PREPARED' and r.status!='HELD':return False
            if e.phase in {'COMMITTED','ACKED'} and r.status!='CONSUMED':return False
            if e.phase=='ABORTED' and r.status!='RELEASED':return False
        return True

def act(s:Composite, c:Command, principal:str)->Optional[Composite]:
    if not s.valid():raise ValueError('invalid state')
    b=s.base
    e=next((e for e in s.effects if e.rid==c.rid),None)
    active=b.lifecycle=='ACTIVE' and not b.shutdown
    # No direct unreserved STORE_WRITE or arbitrary settlement through this interface.
    if c.kind in {'STORE_WRITE','SETTLE_CONSUME','SETTLE_RELEASE'}:return None
    if c.kind=='PREPARE_EFFECT':
        if not active or principal!='worker' or principal in b.revoked or c.token!=b.session or not c.rid or e is not None:return None
        if c.eid in b.seen or not c.eid:return None
        nb=apply(b,replace(c,kind='RESERVE'),principal)
        if nb is None:return None
        result=Composite(nb,s.effects+(Effect(c.rid,principal,b.session,c.value),))
    elif c.kind=='COMMIT_EFFECT':
        if not active or principal!='system' or e is None or e.phase!='PREPARED' or e.generation!=b.session or c.token!=b.session or c.eid in b.seen or not c.eid:return None
        nb=apply(b,replace(c,kind='SETTLE_CONSUME'),principal)
        if nb is None:return None
        nb=replace(nb,store_value=e.payload,effects=nb.effects|{e.rid})
        result=Composite(nb,tuple(replace(v,phase='COMMITTED') if v.rid==e.rid else v for v in s.effects))
    elif c.kind=='ACK_EFFECT':
        if principal!='system' or e is None or e.phase!='COMMITTED' or c.eid in b.seen or not c.eid:return None
        nb=replace(b,seen=b.seen|{c.eid})
        result=Composite(nb,tuple(replace(v,phase='ACKED') if v.rid==e.rid else v for v in s.effects))
    elif c.kind=='ABORT_EFFECT':
        if principal not in {'system','admin'} or e is None or e.phase!='PREPARED' or c.eid in b.seen or not c.eid:return None
        nb=apply(b,replace(c,kind='SETTLE_RELEASE'),principal)
        if nb is None:return None
        result=Composite(nb,tuple(replace(v,phase='ABORTED') if v.rid==e.rid else v for v in s.effects))
    elif c.kind in {'SUSPEND','STOP','RESTORE'}:
        # Invalidate in-flight capabilities and release held reservations, preserving history.
        nb=b
        updated=[]
        for v in s.effects:
            if v.phase=='PREPARED':
                ledger=nb.ledger.settle(v.rid,False)
                if ledger is None:raise AssertionError('ledger inconsistency')
                nb=replace(nb,ledger=ledger)
                updated.append(replace(v,phase='ABORTED'))
            else:updated.append(v)
        nb=apply(nb,c,principal)
        if nb is None:return None
        result=Composite(nb,tuple(updated))
    else:
        nb=apply(b,c,principal)
        if nb is None:return None
        result=Composite(nb,s.effects)
    if not result.valid():raise AssertionError('composite invalid')
    return result
