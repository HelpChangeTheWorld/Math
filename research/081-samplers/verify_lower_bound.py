"""Exact supporting checks for an independent algebraic proof, not proof-by-random-test.
Bits xi use little-endian numbering: xi(x)=(x>>i)&1, i=0,...,5.
No third-party packages. Execute: python verify_lower_bound.py
"""
from itertools import combinations
from collections import Counter
from random import Random
import json
from pathlib import Path

N=64
FULL=(1<<64)-1

def truth_mask(fn):
    return sum(fn(x)<<x for x in range(N))

# The code-theoretic counting lemma: 11 distinct nonzero columns in F2^4.
case_count=0
counts=Counter()
for H in combinations(range(1,16),11):
    reps=Counter(H) # one weight-one vector per column
    for a,b in combinations(H,2):
        reps[a^b]+=1
    for syndrome in range(1,16):
        assert reps[syndrome]>=4
        counts[reps[syndrome]]+=1
        case_count+=1
assert case_count==20475

# All 126 nonconstant affine Boolean functions.
parities=[]
for a in range(1,64):
    for c in range(2):
        f=truth_mask(lambda x,a=a,c=c: ((x&a).bit_count()&1)^c)
        assert f.bit_count()==32
        parities.append((f,('affine',a,c)))

# All 1,800 balanced one-monomial quadratics described in the proof.
quadratics=[]
for i,j in combinations(range(6),2):
    outside=[k for k in range(6) if k not in (i,j)]
    for ai in range(2):
        for aj in range(2):
            for a_small in range(1,16):
                a=sum(1<<k for t,k in enumerate(outside) if (a_small>>t)&1)
                for c in range(2):
                    # f=xi*xj + ai*xi + aj*xj + parity_outside + c.
                    f=truth_mask(lambda x,i=i,j=j,ai=ai,aj=aj,a=a,c=c:
                        ((x>>i&1)*(x>>j&1)) ^ (ai*(x>>i&1)) ^
                        (aj*(x>>j&1)) ^ ((x&a).bit_count()&1) ^ c)
                    assert f.bit_count()==32
                    # Direct width-two transition implementation.
                    def bp(x):
                        state=(x>>i&1)^aj
                        state=(state*((x>>j&1)^ai))^(c^(ai*aj))
                        for k in outside:
                            if a>>k&1:
                                state^=(x>>k&1)
                            # Otherwise the transition preserves the state.
                        return state
                    assert truth_mask(bp)==f
                    quadratics.append((f,('quadratic',i,j,ai,aj,a,c)))
assert len(quadratics)==1800
assert len(set(f for f,_ in quadratics))==1800

# Deterministic smoke checks of explicit witnesses; these do not prove universality.
rng=Random(20261020)
all_tests=parities+quadratics
random_checks=0
first_witness_types=Counter()
example=None
for m in range(1,12):
    for trial in range(4000 if m==11 else 100):
        S=sorted(rng.sample(range(64),m))
        mask=sum(1<<x for x in S)
        witness=None
        for f,desc in all_tests:
            k=(f&mask).bit_count()
            if 4*abs(64*k-m*f.bit_count())>64*m:
                witness={'set':S,'function':desc,'sample_acceptances':k,
                         'full_acceptances':32,'sample_size':m}
                first_witness_types[desc[0]]+=1
                if m==11 and desc[0]=='quadratic' and example is None:
                    example=witness
                break
        assert witness is not None, ('No witness found',S)
        random_checks+=1
out={
    'kind':'exact supporting checks plus deterministic randomized smoke tests',
    'counting_lemma_cases':case_count,
    'number_of_low_weight_representatives_histogram':dict(sorted(counts.items())),
    'affine_functions_verified':len(parities),
    'balanced_quadratics_verified':len(quadratics),
    'all_quadratics_have_full_acceptances':32,
    'all_quadratics_match_explicit_two_state_read_once_program':True,
    'random_sets_checked':random_checks,
    'random_11_point_sets_checked':4000,
    'random_witness_types':dict(first_witness_types),
    'example_11_point_quadratic_witness':example,
    'universal_statement_justification':'The separate algebraic proof, not random testing.',
}
p=Path(__file__).with_name('lower_bound_checks.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
