"""Bounded exploratory MILP, with exact full-class validation for candidates."""
from pathlib import Path
import json,time,sys
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix

ROOT=Path(__file__).parent

def main(k=12):
    fs=np.load(ROOT/'allorders6_truth_tables.npy')
    fs=fs[(fs&1)==0] # discard complement duplicate
    M=np.unpackbits(fs.view(np.uint8).reshape(-1,8),axis=1,bitorder='little')
    sizes=M.sum(axis=1)
    lb=np.maximum(0,np.ceil(k*sizes/64-k/4))
    ub=np.minimum(k,np.floor(k*sizes/64+k/4))
    fixed=np.load(ROOT/'fixed6_truth_tables.npy')
    fixed=fixed[(fixed&1)==0]
    chosen=set(np.searchsorted(fs,fixed).tolist())
    low=np.zeros(64); low[0]=1
    t0=time.time(); log=[]
    rng=np.random.default_rng(731)
    for iteration in range(30):
        ix=np.array(sorted(chosen))
        A=csc_matrix(M[ix,:].astype(float))
        constraints=[LinearConstraint(A,lb[ix],ub[ix]),LinearConstraint(np.ones((1,64)),k,k)]
        remain=150-(time.time()-t0)
        if remain<=0: break
        r=milp(rng.normal(size=64)*0.001,integrality=np.ones(64),bounds=Bounds(low,np.ones(64)),
            constraints=constraints,options={'time_limit':min(30,remain),'mip_rel_gap':0.0})
        entry={'iteration':iteration,'constraints':len(ix),'solver_status':int(r.status),'message':r.message}
        if r.x is None:
            log.append(entry); print(entry,flush=True); break
        S=np.flatnonzero(r.x>0.5)
        counts=M[:,S].sum(axis=1)
        errors=np.abs(counts.astype(np.int64)*64-k*sizes.astype(np.int64))
        w=int(np.argmax(errors))
        violations=np.flatnonzero(errors>16*k)
        entry|={'support':S.tolist(),'worst_numerator':int(errors[w]),'denominator':64*k,
            'witness':hex(int(fs[w])),'uniform_count':int(sizes[w]),'sample_count':int(counts[w]),
            'violations':len(violations),'elapsed':time.time()-t0}
        log.append(entry); print(entry,flush=True)
        if len(violations)==0: break
        # Add diverse maximally violated constraints, preserving exactness of any UNSAT result.
        order=violations[np.argsort(-errors[violations],kind='stable')]
        chosen.update(order[:2000].tolist())
    (ROOT/f'search_allorders_initial_k{k}.json').write_text(json.dumps(log,indent=2)+'\n')

if __name__=='__main__': main(int(sys.argv[1]) if len(sys.argv)>1 else 12)
