"""Step 9 clean-room accounting prototype: one ledger owns quota decisions.
Atomic in-memory transition semantics; no persistence or distributed consensus.
"""
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Account:
    name: str
    limit: int
    spent: int = 0

@dataclass(frozen=True)
class Reservation:
    rid: str
    amount: int
    status: str = 'HELD'

@dataclass(frozen=True)
class Ledger:
    accounts: tuple[Account,...] = (Account('wake',2), Account('attempt',2), Account('resource',3))
    reservations: tuple[Reservation,...] = ()
    used_ids: frozenset[str] = frozenset()
    def account(self, name): return next(a for a in self.accounts if a.name == name)
    def valid(self):
        if tuple(a.name for a in self.accounts)!=('wake','attempt','resource'): return False
        if any(a.limit<0 or not 0<=a.spent<=a.limit for a in self.accounts): return False
        if len({r.rid for r in self.reservations})!=len(self.reservations): return False
        if any(r.amount<=0 or r.status not in {'HELD','CONSUMED','RELEASED'} for r in self.reservations): return False
        if not {r.rid for r in self.reservations}<=self.used_ids: return False
        resource=self.account('resource')
        return sum(r.amount for r in self.reservations if r.status!='RELEASED')<=resource.limit and resource.spent==sum(r.amount for r in self.reservations if r.status=='CONSUMED')
    def charge(self, name):
        a=self.account(name)
        if a.spent>=a.limit:return None
        return replace(self,accounts=tuple(replace(x,spent=x.spent+1) if x.name==name else x for x in self.accounts))
    def reserve(self,rid,amount):
        if not rid or rid in self.used_ids or amount<=0:return None
        outstanding=sum(r.amount for r in self.reservations if r.status!='RELEASED')
        if outstanding+amount>self.account('resource').limit:return None
        return replace(self,reservations=self.reservations+(Reservation(rid,amount),),used_ids=self.used_ids|{rid})
    def settle(self,rid,consume):
        r=next((x for x in self.reservations if x.rid==rid),None)
        if r is None or r.status!='HELD':return None
ac=self.accounts
        if consume:ac=tuple(replace(a,spent=a.spent+r.amount) if a.name=='resource' else a for a in ac)
        return replace(self,accounts=ac,reservations=tuple(replace(x,status='CONSUMED' if consume else 'RELEASED') if x.rid==rid else x for x in self.reservations))

@dataclass(frozen=True)
class Incident:
    name: str
    cycle: str
    recovery: str = 'PENDING'
    activation: str = 'AWAITING_ACK'
    generation: int = 1
    attempts: int = 0
    wakes: int = 0
    deadline: int = 2
    attempt_deadline: int|None = None

@dataclass(frozen=True)
class State:
    ledger: Ledger = Ledger()
    incidents: tuple[Incident,...] = ()
    used_cycles: frozenset[str] = frozenset()
    used_requests: frozenset[tuple[str,int]] = frozenset()
    seen: frozenset[str] = frozenset()
    revoked: frozenset[str] = frozenset()
    lifecycle: str = 'ACTIVE'
    shutdown: bool = False
    session: int = 1
    store_generation: int = 1
    store_value: str = ''
    effects: frozenset[str] = frozenset()
    domain: int = 1
    tick: int = 0
    heartbeat: str = 'RUNNING'
    def valid(self):
        if not self.ledger.valid() or self.lifecycle not in {'ACTIVE','SUSPENDED','STOPPED'}:return False
        if self.session!=self.store_generation or self.session<1 or self.domain<1 or self.tick<0:return False
        if self.shutdown and self.lifecycle!='ACTIVE':return False
        if self.lifecycle!='ACTIVE' and self.heartbeat!='HALTED':return False
        if len({i.name for i in self.incidents})!=len(self.incidents):return False
        if len({i.cycle for i in self.incidents})!=len(self.incidents):return False
        if not {i.cycle for i in self.incidents}<=self.used_cycles:return False
        if not {(i.name,i.generation) for i in self.incidents}<=self.used_requests:return False
        if any(i.attempts<0 or i.attempts>2 or i.wakes<0 or i.wakes>2 or i.generation<1 or (i.recovery=='ACTIVE')!=(i.attempt_deadline is not None) for i in self.incidents):return False
        if any(i.recovery in {'SUCCEEDED','EXHAUSTED','CANCELLED'} and i.activation in {'AWAITING_ACK','ACKNOWLEDGED'} for i in self.incidents):return False
   if self.lifecycle!='ACTIVE' and any(i.recovery in {'PENDING','ACTIVE','FAILED'} for i in self.incidents):return False
        return sum(i.attempts for i in self.incidents)<=self.ledger.account('attempt').spent and sum(i.wakes for i in self.incidents)<=self.ledger.account('wake').spent

@dataclass(frozen=True)
class Command:
    kind: str
    eid: str
    incident: str = ''
    cycle: str = ''
    generation: int|None = None
    token: int|None = None
    rid: str = ''
    amount: int = 0
    tick: int|None = None
    domain: int|None = None
    value: str = ''

ROLES={'CREATE':{'reporter','admin'},'ACK':{'recovery'},'TIMER':{'system'},'SHUTDOWN_INTENT':{'admin'},'SUSPEND':{'admin'},'STOP':{'admin'},'RESUME':{'admin'},'RESTORE':{'admin'},'REPLACE':{'admin'},'REVOKE':{'admin'},'SETTLE_CONSUME':{'system','admin'},'SETTLE_RELEASE':{'system','admin'},'STORE_WRITE':{'worker'},'RESERVE':{'worker'}}

def apply(s:State,c:Command,principal:str)->State|None:
    if not s.valid():raise ValueError('invalid input')
    if not c.eid or c.eid in s.seen or principal not in ROLES.get(c.kind,{'worker','system'}):return None
    x=next((i for i in s.incidents if i.name==c.incident),None)
    k=c.kind; n=None
    def update(i):return replace(s,incidents=tuple(i if v.name==i.name else v for v in s.incidents))
    active=s.lifecycle=='ACTIVE' and not s.shutdown
    if k=='CREATE' and active and x is None and c.incident and c.cycle and c.cycle not in s.used_cycles:
        i=Incident(c.incident,c.cycle,deadline=s.tick+2)
        n=replace(s,incidents=tuple(sorted(s.incidents+(i,),key=lambda z:z.name)),used_cycles=s.used_cycles|{c.cycle},used_requests=s.used_requests|{(i.name,1)})
    elif k=='WAKE' and active and x and s.heartbeat=='RUNNING' and x.activation=='AWAITING_ACK' and x.recovery not in {'SUCCEEDED','EXHAUSTED','CANCELLED'} and s.tick>=x.deadline and x.wakes<2:
        ledger=s.ledger.charge('wake')
        if ledger:n=replace(update(replace(x,wakes=x.wakes+1,deadline=s.tick+2)),ledger=ledger)
    elif k=='ATTEMPT' and active and x and x.recovery=='PENDING' and x.attempts<2:
        ledger=s.ledger.charge('attempt')
        if ledger:n=replace(update(replace(x,recovery='ACTIVE',attempts=x.attempts+1,attempt_deadline=s.tick+3)),ledger=ledger)
    elif k=='ACK' and active and x and x.activation=='AWAITING_ACK' and c.generation==x.generation:n=update(replace(x,activation='ACKNOWLEDGED'))
elif k=='FAIL' and active and x and x.recovery=='ACTIVE':n=update(replace(x,recovery='FAILED',attempt_deadline=None))
    elif k=='RETRY' and active and x and x.recovery=='FAILED' and x.attempts<2:n=update(replace(x,recovery='PENDING'))
    elif k=='EXHAUST' and active and x and x.recovery in {'PENDING','FAILED'} and x.attempts>=2:n=update(replace(x,recovery='EXHAUSTED',activation='FAILED' if x.activation in {'AWAITING_ACK','ACKNOWLEDGED'} else x.activation))
    elif k=='SUCCESS' and active and x and x.recovery=='ACTIVE':n=update(replace(x,recovery='SUCCEEDED',attempt_deadline=None,activation='COMPLETED' if x.activation in {'AWAITING_ACK','ACKNOWLEDGED'} else x.activation))
    elif k=='REPLACE' and active and x and x.activation in {'EXHAUSTED','FAILED','CANCELLED'} and x.recovery not in {'SUCCEEDED','EXHAUSTED','CANCELLED'} and x.wakes<2 and s.ledger.account('wake').spent<s.ledger.account('wake').limit:
        i=replace(x,generation=x.generation+1,activation='AWAITING_ACK',deadline=s.tick+2)
        n=replace(update(i),used_requests=s.used_requests|{(i.name,i.generation)})
    elif k=='TIMER' and active and c.domain==s.domain and c.tick is not None and c.tick>=s.tick:
        inc=[]
        for i in s.incidents:
            if i.recovery=='ACTIVE' and c.tick>=i.attempt_deadline:i=replace(i,recovery='FAILED',attempt_deadline=None)
            if i.activation=='AWAITING_ACK' and i.wakes>=2 and c.tick>=i.deadline:i=replace(i,activation='EXHAUSTED')
            inc.append(i)
        n=replace(s,tick=c.tick,incidents=tuple(inc))
    elif k=='RESERVE' and active and c.token==s.session and principal not in s.revoked:
        ledger=s.ledger.reserve(c.rid,c.amount)
        if ledger:n=replace(s,ledger=ledger)
    elif k in {'SETTLE_CONSUME','SETTLE_RELEASE'}:
        ledger=s.ledger.settle(c.rid,k=='SETTLE_CONSUME')
        if ledger:n=replace(s,ledger=ledger)
    elif k=='STORE_WRITE' and active and c.token==s.store_generation and principal not in s.revoked and c.rid and c.rid not in s.effects:
        n=replace(s,store_value=c.value,effects=s.effects|{c.rid})
    elif k=='REVOKE' and c.incident and principal=='admin':n=replace(s,revoked=s.revoked|{c.incident})
    elif k=='SHUTDOWN_INTENT' and active:n=replace(s,shutdown=True)
    elif k in {'SUSPEND','STOP'} and s.lifecycle=='ACTIVE' and (k=='SUSPEND' or s.shutdown):
        inc=tuple(replace(i,recovery='CANCELLED' if i.recovery not in {'SUCCEEDED','EXHAUSTED','CANCELLED'} else i.recovery,activation='CANCELLED' if i.activation in {'AWAITING_ACK','ACKNOWLEDGED'} else i.activation,attempt_deadline=None) for i in s.incidents)
        n=replace(s,incidents=inc,lifecycle='SUSPENDED' if k=='SUSPEND' else 'STOPPED',heartbeat='HALTED',shutdown=False,session=s.session+1,store_generation=s.store_generation+1)
elif k=='RESUME' and s.lifecycle=='SUSPENDED':n=replace(s,lifecycle='ACTIVE',session=s.session+1,store_generation=s.store_generation+1,domain=s.domain+1,tick=0)
    elif k=='RESTORE' and s.lifecycle!='STOPPED' and not s.shutdown:
        inc=tuple(replace(i,recovery='CANCELLED' if i.recovery not in {'SUCCEEDED','EXHAUSTED','CANCELLED'} else i.recovery,activation='CANCELLED' if i.activation in {'AWAITING_ACK','ACKNOWLEDGED'} else i.activation,attempt_deadline=None) for i in s.incidents)
        n=replace(s,incidents=inc,heartbeat='HALTED',session=s.session+1,store_generation=s.store_generation+1,domain=s.domain+1,tick=0)
    elif k=='HB_START' and active and s.heartbeat=='HALTED':n=replace(s,heartbeat='RUNNING')
    if n is None:return None
    n=replace(n,seen=n.seen|{c.eid})
    if not n.valid():raise AssertionError(('invalid output',k,n))
    if not(s.seen<=n.seen and s.used_cycles<=n.used_cycles and s.used_requests<=n.used_requests and s.revoked<=n.revoked and s.ledger.used_ids<=n.ledger.used_ids and n.session>=s.session):raise AssertionError('authority rollback')
    for name in ('wake','attempt','resource'):
        if n.ledger.account(name).spent<s.ledger.account(name).spent:raise AssertionError('spend rollback')
    return n
