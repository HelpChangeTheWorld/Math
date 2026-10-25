"""Independent fraction-free verification of every saved quartet certificate.

Uses Python arbitrary-precision integer arithmetic and Bareiss elimination,
instead of the generator's vectorized Leibniz determinant expansion.
"""
from pathlib import Path
import itertools
import json
import numpy as np

HERE=Path(__file__).resolve().parent

def det_bareiss(matrix):
    a=[list(map(int,row)) for row in matrix]
    n=len(a);sign=1;previous=1
    for k in range(n-1):
        if a[k][k]==0:
            swap=next((j for j in range(k+1,n) if a[j][k]),None)
            if swap is None:return 0
            a[k],a[swap]=a[swap],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%previous==0
                a[i][j]=value//previous
        for i in range(k+1,n):a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

# Formula coefficient dictionaries: left(a,b,c,d), right(e,f,g,h), output(A,B,C,D).
formulas=[('ad','eh','AD'),('cd','e','C-D'),('a','f-h','BD'),
          ('d','g-e','AC'),('ab','h','-AB'),('c-a','ef','D'),('b-d','gh','A')]

def coeff(expr,alphabet):
    out=[0]*4;sign=1
    for ch in expr:
        if ch=='-':sign=-1
        elif ch=='+':sign=1
        else:
            out[alphabet.index(ch)]+=sign
            sign=1
    return tuple(out)

bases=[[coeff(f[i],alphabet) for f in formulas]
       for i,alphabet in enumerate(('abcd','efgh','ABCD'))]
factors=[[tuple(x*y for x in a for y in b) for a in base for b in base] for base in bases]
grams=[[[sum(x*y for x,y in zip(a,b)) for b in fac] for a in fac] for fac in factors]

# Independently expand the base formula and compare each coefficient of a*b.
for i,j,k in itertools.product(range(4),repeat=3):
    actual=sum(bases[0][r][i]*bases[1][r][j]*bases[2][r][k] for r in range(7))
    expected=int(i%2==j//2 and k//2==i//2 and k%2==j%2)
    assert actual==expected

cert=np.load(HERE/'strassen_4_certificates.npz')
seen=0
for subset,mode,expected1,expected2 in zip(cert['subsets'],cert['mode'],cert['gram_determinant'],cert['khatri_rao_gram_determinant']):
    s=tuple(map(int,subset));m=int(mode)
    assert m in (0,1,2)
    g1=[[grams[m][i][j] for j in s] for i in s]
    g2=[[grams[(m+1)%3][i][j]*grams[(m+2)%3][i][j] for j in s] for i in s]
    d1=det_bareiss(g1);d2=det_bareiss(g2)
    assert d1==int(expected1)>0 and d2==int(expected2)>0
    seen+=1

# Verify completeness and ordering independently of the generation result counts.
assert np.array_equal(cert['subsets'],np.array(list(itertools.combinations(range(49),4))))
assert seen==211876
result={'quartet_certificates_checked':seen,'determinants_independently_recomputed':2*seen,
        'all_certificates_passed':True,'all_quartets_present':True,
        'method':'Python arbitrary-precision integers, fraction-free Bareiss determinant; independently parsed formula coefficients.'}
(HERE/'strassen_four_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
