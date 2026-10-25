"""Independent exact function enumeration; solver proposes, integer verifier checks."""
from pathlib import Path
import json, itertools, math, time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

ROOT=Path(__file__).parent

def enumerate_fixed(n):
    fs={0}
    counts=[1]
    for i in range(n):
        size=1<<i
        mask=(1<<size)-1
        out=set()
        for f in fs:
            gs=(0,mask,f,mask^f)
            out.update(a|(b<<size) for a in gs for b in gs)
        fs=out
        counts.append(len(fs))
    return sorted(fs),counts

def matrix(fs,n):
    return np.array([[(f>>x)&1 for x in range(1<<n)] for f in fs],dtype=np.uint8)

def verify(fs,S,n):
    sm=sum(1<<x for x in S)
    N=1<<n
    k=len(S)
    worst=max((abs(N*(f&sm).bit_count()-k*f.bit_count()),f) for f in fs)
    return {'n':n,'support':S,'k':k,'function_count':len(fs),'max_error_numerator':worst[0],
        'max_error_denominator':N*k,'worst_function_hex':hex(worst[1]),
        'sample_accept_count':(worst[1]&sm).bit_count(),'uniform_accept_count':worst[1].bit_count(),
        'epsilon_one_quarter_pass':4*worst[0]<=N*k}

def main():
    fs,counts=enumerate_fixed(6)
    print('counts',counts,flush=True)
    np.save(ROOT/'fixed6_truth_tables.npy',np.array(fs,dtype=np.uint64))
    M=matrix(fs,6)
    # Complement symmetry: only f(0)=0 necessary. Pin 0 into support by xor-translation symmetry.
    selected=M[:,0]==0
    A=M[selected,:].astype(float)
    sizes=A.sum(axis=1)
    k=8
    lb=np.maximum(0,np.ceil(k*sizes/64-k/4))
    ub=np.minimum(k,np.floor(k*sizes/64+k/4))
    bounds_lo=np.zeros(64); bounds_lo[0]=1
    constraints=[LinearConstraint(A,lb,ub),LinearConstraint(np.ones((1,64)),k,k)]
    t=time.time()
    r=milp(np.zeros(64),integrality=np.ones(64),bounds=Bounds(bounds_lo,np.ones(64)),
        constraints=constraints,options={'time_limit':180,'mip_rel_gap':0})
    print('solver',r.message,'seconds',time.time()-t,flush=True)
    result={'counts':counts,'solver_message':r.message}
    if r.x is not None:
        S=np.flatnonzero(r.x>0.5).tolist()
        result['fixed']=verify(fs,S,6)
        print('fixed',result['fixed'],flush=True)
        # Test the same support against every variable order. Permuting support rather than truth tables.
        worst=None
        for perm in itertools.permutations(range(6)):
            Sp=[sum(((x>>perm[i])&1)<<i for i in range(6)) for x in S]
            v=verify(fs,Sp,6)
            if worst is None or v['max_error_numerator']>worst['max_error_numerator']:
                worst=v|{'permutation':list(perm),'original_support':S}
        result['all_orders_worst']=worst
        print('all_orders',worst,flush=True)
    (ROOT/'audit_results.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': main()
