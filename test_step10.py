import unittest
from dataclasses import replace
from model import Composite, act
from step9 import Command

def c(kind,eid,rid='',**kw):return Command(kind,eid,rid=rid,**kw)
class Tests(unittest.TestCase):
 def setUp(self):self.s=Composite()
 def prepare(self):return act(self.s,c('PREPARE_EFFECT','p','r',amount=2,token=1,value='X'),'worker')
 def commit(self,s):return act(s,c('COMMIT_EFFECT','m','r',token=1),'system')
 def test_unreserved_write_rejected(self):self.assertIsNone(act(self.s,c('STORE_WRITE','w','r',token=1,value='X'),'worker'))
 def test_direct_settlement_rejected(self):self.assertIsNone(act(self.s,c('SETTLE_CONSUME','z','r'),'system'))
 def test_prepare_holds_capacity(self):
  s=self.prepare();self.assertEqual(s.base.ledger.reservations[0].status,'HELD');self.assertEqual(s.base.ledger.account('resource').spent,0)
 def test_commit_consumes_and_writes(self):
  s=self.commit(self.prepare());self.assertEqual(s.base.store_value,'X');self.assertEqual(s.base.ledger.account('resource').spent,2)
 def test_commit_retry_idempotence(self):
  s=self.commit(self.prepare());self.assertIsNone(self.commit(s));self.assertEqual(s.base.ledger.account('resource').spent,2)
 def test_ack_after_commit(self):
  s=self.commit(self.prepare());t=act(s,c('ACK_EFFECT','a','r'),'system');self.assertEqual(t.effects[0].phase,'ACKED');self.assertIsNone(act(t,c('ACK_EFFECT','a2','r'),'system'))
 def test_crash_before_commit(self):
  s=self.prepare();t=act(s,c('RESTORE','restore'),'admin');self.assertEqual(t.effects[0].phase,'ABORTED');self.assertEqual(t.base.ledger.account('resource').spent,0);self.assertIsNone(self.commit(t))
 def test_crash_after_commit_before_ack(self):
  s=self.commit(self.prepare());t=act(s,c('RESTORE','restore'),'admin');self.assertEqual(t.effects[0].phase,'COMMITTED');self.assertEqual(t.base.ledger.account('resource').spent,2);self.assertEqual(act(t,c('ACK_EFFECT','a','r'),'system').effects[0].phase,'ACKED')
 def test_shutdown_intent_fences_effects(self):
  s=act(self.prepare(),c('SHUTDOWN_INTENT','si'),'admin');self.assertIsNone(self.commit(s));self.assertIsNone(act(s,c('PREPARE_EFFECT','p2','r2',amount=1,token=1),'worker'))
 def test_suspend_fences_stale_generation(self):
  s=act(self.prepare(),c('SUSPEND','suspend'),'admin');self.assertIsNone(self.commit(s));self.assertEqual(s.effects[0].phase,'ABORTED')
 def test_revocation_fences_prepare(self):
  s=act(self.s,c('REVOKE','rv',incident='worker'),'admin');self.assertIsNone(act(s,c('PREPARE_EFFECT','p','r',amount=1,token=1),'worker'))
 def test_capacity_conservation(self):
  s=self.prepare();self.assertIsNone(act(s,c('PREPARE_EFFECT','p2','r2',amount=2,token=1),'worker'));s=self.commit(s);self.assertIsNone(act(s,c('PREPARE_EFFECT','p3','r3',amount=2,token=1),'worker'))
 def test_no_reuse_aborted_id(self):
  s=act(self.prepare(),c('ABORT_EFFECT','abort','r'),'admin');self.assertIsNone(act(s,c('PREPARE_EFFECT','p2','r',amount=1,token=1),'worker'))
 def test_untrusted_commit_rejected(self):self.assertIsNone(act(self.prepare(),c('COMMIT_EFFECT','m','r',token=1),'worker'))
 def test_invalid_input_detected(self):
  s=self.prepare();bad=replace(s,effects=(replace(s.effects[0],phase='ACKED'),));self.assertFalse(bad.valid())
if __name__=='__main__':unittest.main()
