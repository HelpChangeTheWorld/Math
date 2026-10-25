"""Independent direct extension check for a 3-flip-necessary witness.
Does not import the search, its sequence encoding, buckets or BFS.
"""
from pathlib import Path
import itertools,json,time
import numpy as np
OUT=Path(__file__).resolve().parent
P=np.array([[1,-1,-1,-1,1,1,-1]]*3+[[1,1,1,-1,1,1,1]],dtype=np.int64)
APP=np.array(list(itertools.product((-1,1),repeat=8)),dtype=np.int64).reshape(256,4,2)
allowed=[(r,j) for r in range(4) for j in range(1,7)]
def correlations(batch):
    return np.stack([(batch*np.roll(batch,-t,axis=2)).sum(axis=(1,2)) for t in range(1,batch.shape[2])],axis=1)
assert np.all(correlations(P[None,:,:])==0)
tests={}; t0=time.monotonic()
for d in range(3):
    count=0;hits=0
    for flips in itertools.combinations(allowed,d):
        q=P.copy()
        for r,j in flips:q[r,j]*=-1
        candidates=np.concatenate([np.repeat(q[None,:,:],256,axis=0),APP],axis=2)
        good=np.all(correlations(candidates)==0,axis=1)
        hits+=int(good.sum());count+=256
    assert hits==0
    tests[str(d)]={"extensions_checked":count,"valid":hits}
extension=np.array([[1,1,-1,-1,1,-1,-1,1,-1],
 [1,-1,-1,-1,1,1,1,1,1],
 [1,-1,-1,-1,1,1,-1,1,-1],
 [1,1,1,-1,1,1,1,-1,1]],dtype=np.int64)
assert np.all(correlations(extension[None,:,:])==0)
changes=np.argwhere(extension[:,:7]!=P).tolist()
assert changes==[[0,1],[0,5],[1,6]]
assert np.all(extension[:,0]==1)
result={"original_parent":P.tolist(),"normalization":"first sign+1 in each row; fixed row and position order",
"repair_rule":"any noninitial old signs may flip; repaired old prefix need not remain complementary",
"negative_checks":tests,"total_negative_candidates":sum(v["extensions_checked"] for v in tests.values()),
"three_flip_extension":extension.tolist(),"changed_positions_zero_based_row_column":changes,
"parent_all_nonzero_shift_sums":correlations(P[None,:,:])[0].tolist(),
"extension_all_nonzero_shift_sums":correlations(extension[None,:,:])[0].tolist(),
"minimum_flips_exactly":3,"seconds":time.monotonic()-t0}
(OUT/"witness_verification.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result))

