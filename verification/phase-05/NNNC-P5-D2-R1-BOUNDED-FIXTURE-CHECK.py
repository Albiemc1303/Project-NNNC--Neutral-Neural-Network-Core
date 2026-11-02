"""Illustrative finite fixture checks; NOT a proof of NNNC formal contracts."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Occ:
    origin: str
    input_bound: bool
    no_external: bool
    delivered_hidden: bool

@dataclass(frozen=True)
class Episode:
    budget: int
    steps: tuple[int, ...]
    terminal: str

def check_occ(o):
    return (o.origin in {'INTERNAL','EXTERNAL'}
            and o.no_external == (o.origin == 'INTERNAL')
            and (not o.delivered_hidden or o.input_bound))

def check_scrutiny(anomaly_lost, cue_delivered, action):
    return not anomaly_lost or (cue_delivered and action in {'SCRUTINIZE','DEFER'})

def check_memory(fs_transport, authorized_commit, overwrite_original):
    return not overwrite_original and (not authorized_commit or fs_transport)

def check_learning(fb_applicable, claimed_update, alternative_typed):
    return not (claimed_update and not fb_applicable) or alternative_typed

def check_episode(e):
    return (e.budget >= 0 and len(e.steps) <= e.budget
            and len(set(e.steps)) == len(e.steps)
            and e.terminal in {'CHOICE','UNRESOLVED','DEFER','FAILURE'})

CASES = [
    ('valid internal binding', check_occ(Occ('INTERNAL',True,True,True)), True),
    ('CE-P5-12 input bypass', check_occ(Occ('INTERNAL',False,True,True)), False),
    ('valid metadata loss with scrutiny', check_scrutiny(True,True,'SCRUTINIZE'), True),
    ('CE-P5-13 suppressed metadata loss', check_scrutiny(True,False,'CHOICE'), False),
    ('valid authorized memory access', check_memory(True,True,False), True),
    ('CE-P5-14 original overwrite', check_memory(True,True,True), False),
    ('valid alternate learning path', check_learning(False,True,True), True),
    ('CE-P5-15 untyped alternative', check_learning(False,True,False), False),
    ('valid bounded episode', check_episode(Episode(2,(1,2),'DEFER')), True),
    ('CE-P5-15 excess loop', check_episode(Episode(2,(1,2,3),'CHOICE')), False),
    ('CE-P5-15 repeated iteration', check_episode(Episode(2,(1,1),'CHOICE')), False),
]
if __name__=='__main__':
    for name,actual,expected in CASES:
        assert actual == expected, f'{name}: expected {expected}, got {actual}'
        print(f'PASS | {name} | accepted={actual}')
    print(f'ALL {len(CASES)} ILLUSTRATIVE FIXTURES PASSED; NOT A FORMAL PROOF')