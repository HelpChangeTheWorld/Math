"""Independent direct flattening-minor certificates for all Strassen-square triples."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
from collections import Counter
import runpy,json,math
P=Path(__file__).parent
s=runpy.run_path(str(P/'computation_priority.py'))
U,V,W=[s[n] for n in ['U','V','W']]
for ai in range(4):
 for bi in range(4):
  actual=[sum(U[t][ai]*V[t][bi]*W[t][ci]for t in range(7))for ci in range(4)]
  expected=[0]*4
  if ai%2==bi//2:expected[2*(ai//2)+bi%2]=1
  assert actual==expected
modes=[[[a*b for a in src[i]for b in src[j]]for i in range(7)for j in range(7)]for src in [U,V,W]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def determinant(a):return dot(a[0],cross(a[1],a[2]))
def independent_rows(rows):
 basis=[];inds=[];normal=None
 for index,row in enumerate(rows):
  if not basis:
   if any(row):basis.append(row);inds.append(index)
  elif len(basis)==1:
   normal=cross(basis[0],row)
   if any(normal):basis.append(row);inds.append(index)
  elif dot(normal,row):
   return inds+[index],basis+[row]
 return None
certs=[];mcount=Counter();detcount=Counter()
for ids in combinations(range(49),3):
 for mode in range(3):
  A=modes[mode];B=modes[(mode+1)%3];C=modes[(mode+2)%3]
  left=independent_rows([[A[t][r]for t in ids]for r in range(16)])
  if left is None:continue
  right=independent_rows(([B[t][b]*C[t][c]for t in ids]for b in range(16)for c in range(16)))
  assert right is not None,(ids,mode)
  rows,L=left;cols,R=right
  # This is a direct 3x3 minor of the ACTUAL flattened sum of three tensors.
  # Not just ranks of the three left factor vectors.
  minor=[[sum(A[t][r]*B[t][col//16]*C[t][col%16]for t in ids)for col in cols]for r in rows]
  d=determinant(minor);assert d!=0,(ids,mode,minor)
  assert d==determinant(L)*determinant(R)
  certs.append({'terms':ids,'flattening_mode':mode,'rows':rows,'columns':cols,'minor_determinant':d})
  mcount[mode]+=1;detcount[d]+=1
  break
 else:raise AssertionError(('No nonzero minor',ids))
assert len(certs)==math.comb(49,3)==18424
(P/'captain_strassen_minor_certificates.json').write_text(json.dumps(certs,separators=(',',':')))
# Independently expand the elementary integrals after u=sqrt(2x+1).
# The upper endpoint is sqrt3; powers yield rational values after division by sqrt3.
I0=F(3)-F(9,5)
I1=(F(36,5)-F(27,7)-F(3))/2
report={
 'review_scope':'Independent same-workflow audit of items93 and100 only; no novelty claim or external endorsement.',
 '93':{'verdict':'CONFIRMED','independent_matrix_unit_product_checks':16,'triples_with_direct_nonzero_flattening_minor':len(certs),'mode_counts':dict(mcount),'minor_determinant_counts':dict(detcount),'certificates':'captain_strassen_minor_certificates.json', 'proof':'A sum of two rank-one three-tensors has every matrix flattening of rank at most2. Every tested triple has an explicitly computed nonzero3x3 minor in one actual flattening, hence tensor rank at least3. The given three-term expression supplies rank at most3, so every triple has tensor rank exactly3 over Q (and C). Thus none admits an exact local3-to2 replacement, with all other terms held fixed and no coefficient-alphabet restriction.', 'original_shortcut_justification':'Three rank-one matrices b_i c_i^T are independent when both triples have pairwise nonproportional members: a nontrivial combination of two has matrix rank2 if both coefficients are nonzero, so cannot equal the third rank-one matrix. Zero coefficients reduce to forbidden proportionality. The factor-span shortcut was therefore valid here; direct minors independently avoid relying on it.', 'limits':'Does not exclude modifying four or more terms, changing the full decomposition, approximate/border-rank constructions, or faster general matrix multiplication.'},
 '100':{'verdict':'CONFIRMED with positive integral convention I_j=2 integral x^j sqrt(2(h−V(x))) dx','endpoint_h':'1/6','x_interval':['-1/2','1'],'factorization':'2(h−V(x))=(1−x)^2(2x+1)/3','substitution':'u=sqrt(2x+1); I0=(1/sqrt3) integral_0^sqrt3 (3u^2−u^4)du; I1=(1/(2sqrt3)) integral_0^sqrt3 (4u^4−u^6−3u^2)du','I0':str(I0),'I1':str(I1),'ratio':str(I1/I0),'interior_zero':'Since I0>0, |I1/I0|≤max|x|→0 as h→0. Continuity and endpoint ratio1/7 imply I1/I0=1/10 at some interior h. This does not establish a simple zero or a global cycle-count bound.'}}
(P/'captain_priority_audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps({'93':report['93']['verdict'],'triples':len(certs),'100':{'I0':str(I0),'I1':str(I1)}}))
