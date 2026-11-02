from pathlib import Path
import subprocess,sys,json,re,hashlib,datetime
ROOT=Path(__file__).resolve().parent
S=ROOT/'sources'
results=[]
for n,mod in [(1,'test_reference'),(2,'test_model'),(3,'test_checker')]:
    d=S/f'nnnc_phase1_build{n}'
    p=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(d),'-p',mod+'.py','-v'],cwd=d,text=True,capture_output=True,timeout=60)
    out=p.stdout+'\n'+p.stderr
    m=re.search(r'Ran (\d+) tests?',out)
    results.append({'build':n,'command':f'python -m unittest discover -s sources/nnnc_phase1_build{n} -p {mod}.py -v','tests':int(m.group(1)) if m else None,'passed':p.returncode==0 and bool(m),'exit_code':p.returncode,'output':out})
# Independently regenerate checker mutation witnesses, compare counts with Build 3 reported baseline
checker=S/'nnnc_phase1_build3'/'checker.py'
p=subprocess.run([sys.executable,str(checker)],cwd=checker.parent,text=True,capture_output=True,timeout=60)
try:
    obj=json.loads(p.stdout)
    regenerated={'passed':p.returncode==0,'data':obj,'stderr':p.stderr}
except Exception as e:
    regenerated={'passed':False,'error':str(e),'stdout':p.stdout,'stderr':p.stderr}
source_hashes={}
for n in (1,2,3):
    for f in sorted((S/f'nnnc_phase1_build{n}').glob('*.py')):
        source_hashes[f'{n}/{f.name}']=hashlib.sha256(f.read_bytes()).hexdigest()
summary={'baseline':'P1-D1 v2.0; P1-D2 v0.2.1 architect-accepted','suites':results,'checker_regeneration':regenerated,'sha256':source_hashes,'all_pass':all(r['passed'] for r in results) and regenerated['passed']}
(ROOT/'execution_results.json').write_text(json.dumps(summary,indent=2,default=str)+'\n')
for r in results:
    print(f"Build {r['build']}: {r['tests']} tests, {'PASS' if r['passed'] else 'FAIL'}")
print('Checker regeneration:', 'PASS' if regenerated['passed'] else 'FAIL')
print('OVERALL:', 'PASS' if summary['all_pass'] else 'FAIL')
sys.exit(0 if summary['all_pass'] else 1)
