"""Independent full Cartesian enumeration; no correlation bucketing."""
import itertools,json
from pathlib import Path
import numpy as np

res={}
for n in (3,5):
    seq=np.array([(1,)+tail for tail in itertools.product((-1,1),repeat=n-1)],dtype=np.int16)
    quad=seq[np.array(list(itertools.product(range(len(seq)),repeat=4)))]
    corr=np.stack([(quad*np.roll(quad,-s,axis=2)).sum(axis=(1,2)) for s in range(1,n)],axis=1)
    valid=quad[(corr==0).all(axis=1)]
    res[str(n)]={'all_ordered_normalized_quadruples':len(quad),'valid_count_direct_all_shifts':len(valid)}
    if n==3: parents={tuple(v.flat) for v in valid}
    if n==5:
        prefixes={tuple(v[:,:3].flat) for v in valid}
        res['3_to_5']={'distinct_extendable_prefixes':len(prefixes),'valid_parents_extendable':len(parents&prefixes),'valid_parents':len(parents)}
(Path(__file__).parent/'hadamard_small_independent.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res))
