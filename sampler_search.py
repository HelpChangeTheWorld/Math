"""Correlated uniform six-bit support search; exact post-verification.

The mathematical class is generated with exact bit operations. SciPy/HiGHS
only proposes a binary support; every reported success is checked exactly
against every function. Solver infeasibility alone is not a formal certificate.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json, time, sys
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix, vstack
import scipy

ROOT=Path(__file__).parent


def block_pairs():
    pairs={}
    for layers in product(range(16),repeat=3):
        masks=[]
        for initial in (0,1):
            mask=0
            for x in range(8):
                s=initial
                for j,t in enumerate(layers):s=(t>>(2*s+((x>>(2-j))&1)))&1
                mask|=s<<x
            masks.append(mask)
        pairs.setdefault(tuple(masks),list(layers))
    return pairs


def complete_functions():
    pairs=block_pairs()
    first={a for a,b in pairs}
    functions={sum((g1 if f>>a&1 else g0)<<(8*a) for a in range(8))
               for f in first for g0,g1 in pairs}
    assert len(pairs)==520 and len(first)==88 and len(functions)==18664
    return sorted(functions)


def exact_verify(functions,support):
    k=len(support);mask=sum(1<<x for x in support)
    worst=Fraction(0);witness=None
    for f in functions:
        delta=abs(Fraction((mask&f).bit_count(),k)-Fraction(f.bit_count(),64))
        if delta>worst:worst=delta;witness=f
    return {'support':support,'binary_strings':[format(x,'06b') for x in support],
            'maximum_error':str(worst),'passes_quarter':worst<=Fraction(1,4),
            'witness_function_mask':witness,
            'witness_full_accepted':witness.bit_count() if witness is not None else 0,
            'witness_sample_accepted':(mask&witness).bit_count() if witness is not None else 0}


def main():
    k=int(sys.argv[1]) if len(sys.argv)>1 else 16
    limit=float(sys.argv[2]) if len(sys.argv)>2 else 90
    functions=complete_functions()
    (ROOT/'sampler_function_masks.json').write_text(json.dumps(functions)+'\n')
    # Complemented functions impose exactly the same absolute-error constraint.
    full=(1<<64)-1
    representatives=[f for f in functions if f<(full^f)]
    A=np.array([[(f>>x)&1 for x in range(64)] for f in representatives],dtype=float)
    b=np.array([f.bit_count() for f in representatives],dtype=float)
    # |sum_S f/k - sum_U f/64| <=1/4. Integral sums permit rounding bounds.
    lower=np.ceil(k*b/64-k/4-1e-10)
    upper=np.floor(k*b/64+k/4+1e-10)
    A=vstack([csc_matrix(A),csc_matrix(np.ones((1,64)))],format='csc')
    lower=np.append(lower,k);upper=np.append(upper,k)
    low=np.zeros(64);high=np.ones(64)
    # Translating all strings by xor preserves the function class. Some
    # translate of every nonempty candidate contains0, so this loses none.
    low[0]=high[0]=1
    started=time.monotonic()
    result=milp(np.zeros(64),integrality=np.ones(64),bounds=Bounds(low,high),
                constraints=LinearConstraint(A,lower,upper),
                options={'time_limit':limit,'mip_rel_gap':0.0,'presolve':True})
    record={'model':'six bits, fixed order, width2, start0, arbitrary acceptance',
            'complete_function_count':len(functions),'complement_representatives':len(representatives),
            'requested_support_size':k,'solver':'scipy.optimize.milp / HiGHS',
            'scipy_version':scipy.__version__,'time_limit_seconds':limit,
            'elapsed_seconds':time.monotonic()-started,'solver_status':int(result.status),
            'solver_message':result.message,'claim_status':'No novelty or general derandomization claim.'}
    if result.x is not None and np.max(abs(result.x-np.round(result.x)))<1e-6:
        support=[i for i,x in enumerate(result.x) if x>0.5]
        if len(support)==k:
            record['exact_verification']=exact_verify(functions,support)
    record['interpretation']='A candidate counts as success only if exact_verification.passes_quarter is true. Infeasibility/timeout is only the solver report unless independently certified.'
    path=ROOT/f'sampler_search_{k}.json'
    path.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))


if __name__=='__main__':main()
