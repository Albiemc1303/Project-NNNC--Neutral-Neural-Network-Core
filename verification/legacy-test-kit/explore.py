from collections import deque
from model import Composite,act
from step9 import Command

def events(depth):
 t=depth+1
 return [
 (Command('PREPARE_EFFECT',f'p{t}',rid='r1',amount=1,token=1,value='A'),'worker'),
 (Command('PREPARE_EFFECT',f'q{t}',rid='r2',amount=2,token=1,value='B'),'worker'),
 (Command('COMMIT_EFFECT',f'c{t}',rid='r1',token=1),'system'),
 (Command('COMMIT_EFFECT',f'd{t}',rid='r2',token=1),'system'),
 (Command('ACK_EFFECT',f'a{t}',rid='r1'),'system'),
 (Command('ACK_EFFECT',f'b{t}',rid='r2'),'system'),
 (Command('ABORT_EFFECT',f'x{t}',rid='r1'),'admin'),
 (Command('ABORT_EFFECT',f'y{t}',rid='r2'),'admin'),
 (Command('RESTORE',f'r{t}'),'admin'),
 (Command('SHUTDOWN_INTENT',f's{t}'),'admin'),
 (Command('SUSPEND',f'u{t}'),'admin'),
 ]

def run(depth_limit=5):
 start=Composite(); seen={start};q=deque([(start,0)]);accepted=rejected=0
 while q:
  s,d=q.popleft()
  if d==depth_limit:continue
  for cmd,principal in events(d):
   n=act(s,cmd,principal)
   if n is None:rejected+=1;continue
   accepted+=1
   assert n.valid()
   assert n.base.ledger.account('resource').spent>=s.base.ledger.account('resource').spent
   assert s.base.ledger.used_ids<=n.base.ledger.used_ids
   if n not in seen:seen.add(n);q.append((n,d+1))
 print(f'depth={depth_limit} states={len(seen)} accepted_decisions={accepted} rejected_decisions={rejected} invariant_violations=0')
if __name__=='__main__':run()
