"""Exact local flattening audit of the standard Strassen tensor square.

This reconstructs a standard seven-product decomposition explicitly below.
It does not assume identity with a missing historical coefficient file.
All determinant arithmetic is integer (no floating point or modular ranks).
"""
from pathlib import Path
import itertools
import json
import math
import numpy as np

HERE = Path(__file__).resolve().parent

# Each row is one product; coordinates are row-major (00,01,10,11).
A0 = np.array([[1,0,0,1],[0,0,1,1],[1,0,0,0],[0,0,0,1],
               [1,1,0,0],[-1,0,1,0],[0,1,0,-1]],dtype=np.int64)
B0 = np.array([[1,0,0,1],[1,0,0,0],[0,1,0,-1],[-1,0,1,0],
               [0,0,0,1],[1,1,0,0],[0,0,1,1]],dtype=np.int64)
C0 = np.array([[1,0,0,1],[0,0,1,-1],[0,1,0,1],[1,0,1,0],
               [-1,1,0,0],[0,0,0,1],[1,0,0,0]],dtype=np.int64)

def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def batch_determinant(m):
    """Leibniz determinant for integer matrices of dimension at most four."""
    k=m.shape[-1]
    ans=np.zeros(m.shape[0],dtype=np.int64)
    for p in itertools.permutations(range(k)):
        v=np.ones(m.shape[0],dtype=np.int64)
        for i,j in enumerate(p):
            v*=m[:,i,j]
        ans+=parity(p)*v
    return ans

def known_multiplication_tensor():
    t=np.zeros((4,4,4),dtype=np.int64)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                t[2*i+j,2*j+k,2*i+k]=1
    return t

base=np.einsum('ri,rj,rk->ijk',A0,B0,C0)
assert np.array_equal(base,known_multiplication_tensor())
A=np.array([np.kron(a,b) for a in A0 for b in A0],dtype=np.int64)
B=np.array([np.kron(a,b) for a in B0 for b in B0],dtype=np.int64)
C=np.array([np.kron(a,b) for a in C0 for b in C0],dtype=np.int64)
square=np.einsum('ri,rj,rk->ijk',A,B,C)
assert np.array_equal(square,np.einsum('ijk,abc->iajbkc',base,base).reshape(16,16,16))

grams=[X@X.T for X in (A,B,C)]
report={
  'model':'Explicit standard seven-term Strassen decomposition tensored with itself; 49 fixed integer rank-one terms.',
  'base_identity_verified':True,
  'tensor_square_identity_verified':True,
  'term_numbering':'0-based; term7*i+j is base term i tensored with base term j.',
  'arithmetic':'numpy int64 exact integer Leibniz determinants, dimension<=4; conservative absolute intermediate bound24*16**4=1572864 below2**63.',
  'rank_certificate':'For a selected k-term subset and a mode, det Gram(mode factors)>0 and det Gram(Khatri-Rao(other two factors))>0 imply that flattening has rank k over Q and C.',
  'historical_file_comparison':'Original old coefficient archive was unavailable; identity with that archive is not asserted.'
}

for k in (3,4):
    subsets=np.array(list(itertools.combinations(range(49),k)),dtype=np.int16)
    g=[G[subsets[:,:,None],subsets[:,None,:]] for G in grams]
    d=[batch_determinant(x) for x in g]
    pair=[batch_determinant(g[(i+1)%3]*g[(i+2)%3]) for i in range(3)]
    assert all((x>=0).all() for x in d+pair)
    mode=np.full(len(subsets),-1,dtype=np.int8)
    d1=np.zeros(len(subsets),dtype=np.int64)
    d2=np.zeros(len(subsets),dtype=np.int64)
    for i in range(3):
        ok=(mode<0)&(d[i]>0)&(pair[i]>0)
        mode[ok]=i
        d1[ok]=d[i][ok]
        d2[ok]=pair[i][ok]
    survivors=subsets[mode<0]
    np.savez_compressed(HERE/f'strassen_{k}_certificates.npz',subsets=subsets,mode=mode,gram_determinant=d1,khatri_rao_gram_determinant=d2)
    report[str(k)]={
      'subsets':int(len(subsets)),
      'expected_subsets':math.comb(49,k),
      'certified_rank_k_flattening':int(np.count_nonzero(mode>=0)),
      'survivors':survivors.tolist(),
      'survivor_count':len(survivors),
      'certificate_counts_by_mode':[int(np.count_nonzero(mode==i)) for i in range(3)],
      'maximum_gram_determinant':max(int(x.max()) for x in d),
      'maximum_khatri_rao_gram_determinant':max(int(x.max()) for x in pair),
    }
    print(json.dumps({'k':k,**{a:b for a,b in report[str(k)].items() if a!='survivors'}},sort_keys=True),flush=True)

report['interpretation']='Each certified quartet needs at least four rank-one tensor terms, so cannot be replaced by three while other45 terms remain fixed. A survivor would require further work; deficient flattening does not imply compressibility. No rank49 lower bound or matrix multiplication exponent theorem follows.'
(HERE/'strassen_four_results.json').write_text(json.dumps(report,indent=2)+'\n')
