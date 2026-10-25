"""Reproduce original certificate with x1 leftmost, explicitly converting indexing."""
import json,itertools
from pathlib import Path
from audit_fixed import enumerate_fixed,verify

ROOT=Path(__file__).parent
fs,counts=enumerate_fixed(6)
original=[0,4,13,14,26,31,33,35]
S=[int(format(x,'06b')[::-1],2) for x in original]
r=verify(fs,S,6)
r['source_support_msb_x1']=original
r['source_strings_x1_leftmost']=[format(x,'06b') for x in original]
worst=None
for perm in itertools.permutations(range(6)):
    Sp=[sum(((x>>perm[i])&1)<<i for i in range(6)) for x in S]
    w=verify(fs,Sp,6)
    if worst is None or w['max_error_numerator']>worst['max_error_numerator']:
        worst=w|{'permutation':[i+1 for i in perm]}
r['all_orders_worst']=worst
(ROOT/'original_support_verification.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
