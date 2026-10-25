"""Bounded independent checks of four priority outputs; no full number-script rerun."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import product
import json
P=Path(__file__).parent
read=lambda i:json.loads((P/f'number_{i}.json').read_text())
checks={}
# 6: verify every symbolic affine record; parity class independence follows since
# adding4096 to n shifts the t-step value by an even integer for t<12.
d=read(6);exceptions=[]
for row in d['rows']:
 A,B,den=1,0,1
 r=row['r']
 for bit in row['parity_word']:
  representative=r or 4096
  assert (A*representative+B)%den==0
  assert ((A*representative+B)//den)%2==bit
  if bit:A,B=3*A,3*B+den
  den*=2
 assert (A,B)==(row['A'],row['B']) and den==4096
 assert A==3**row['odd_steps']
 assert row['D']==4096-A
 if row['D']>0:
  threshold=B//row['D']+1
  assert threshold==row['minimum_integer_for_descent']
  expected=list(range(r or 4096,threshold,4096))
  assert expected==row['finite_non_descending_representatives']
  exceptions.extend(expected)
expected_count=sum(comb(12,k)for k in range(8))
assert expected_count==d['eventually_descending_classes']==3302
checks['6']={'verdict':'confirmed','symbolic_records_checked':4096,'contracting_count_binomial_check':expected_count,'noncontracting_count':4096-expected_count,'finite_exceptions':exceptions,'scope':'The3302 classes descend AT STEP12 for all sufficiently large starts within the class. The794 others do not descend at that step; no eventual-orbit classification is implied. The parity itinerary is constant modulo4096 for12 one-division steps by induction.'}
# 8: independently compare all exact stored mass fractions to both baselines.
d=read(8);comparisons=[]
for row in d['configurations']:
 b=next(x for x in d['baselines']if x['lo']==row['lo'])
 mass=F(row['prime_pair_numerator'],row['total_numerator'])
 assert mass==F(row['normalized_prime_pair_mass'])
 comparisons.append({'R':row['R'],'j':row['j'],'lo':row['lo'],'above_unweighted':mass>F(b['unweighted_fraction']),'below_wheel':mass<F(b['wheel_fraction'])})
assert all(x['above_unweighted']and x['below_wheel']for x in comparisons)
checks['8']={'verdict':'confirmed from code inspection and exact comparison of stored totals','configurations_compared':len(comparisons),'conclusion':'All six weights beat unweighted prime-pair fractions but lose to the30-wheel baseline in both intervals. This is normalized weighted mass, not classifier accuracy or asymptotic prime detection.','scope':'Did not recompute every divisor sum. Inspected Möbius coefficients, n(n+2) divisibility, squared common-denominator weights, prime-pair indicators, and matching interval endpoints; no error found.'}
# 23: direct group enumeration and cubic facts.
d=read(23);G=[];H=[]
for a,b,c,e in product([0,1],repeat=4):
 if (a*e-b*c)%2:
  G.append((a,b,c,e))
  if a==1 and c==0:H.append((a,b,c,e))
assert len(G)==6 and sum((a+e)%2 for a,b,c,e in G)==2
assert len(H)==2 and all((a+e)%2==0 for a,b,c,e in H)
assert -4*(-1)**3-27*1**2==-23
checks['23']={'verdict':'confirmed','full_group_order':6,'trace_one_count':2,'stabilizer_order':2,'stabilizer_trace_one_count':0,'proof':'x^3−x+1 has no rational root and discriminant−23, giving S3≅GL2(F2). The second cubic factors (x−1)(x²+x−1), with quadratic discriminant5, giving the order-two point stabilizer.','scope':'These are group-image fractions. Frobenius interpretations require odd good primes (exclude2,23 for E1 and2,5 for E2). No higher-modulus independence follows.'}
# 32: independent reverse-Horner rational arctangent partial sums.
def atan_interval(q,K):
 a=F(0)
 for j in reversed(range(K)):a=F((-1)**j,2*j+1)+a/(q*q)
 a/=q
 eps=F(1,(2*K+1)*q**(2*K+1))
 return (a,a+eps)if K%2==0 else(a-eps,a)
a,b=atan_interval(5,1000),atan_interval(239,300)
lo,hi=16*a[0]-4*b[1],16*a[1]-4*b[0]
low=((lo-3)*2**4096).__floor__();high=((hi-3)*2**4096).__floor__()
assert low==high
assert f'{low:01024x}'==read(32)['fractional_binary_hex']
bits=f'{low:04096b}'
def D1(n):return abs(F(bits[:n].count('1'),n)-F(1,2))
assert D1(1024)==F(11,1024) and D1(2048)==F(31,2048)
assert D1(2048)>D1(1024)
checks['32']={'verdict':'confirmed with independent rational interval recomputation','certified_digits':4096,'hex_matches_saved_output':True,'one_bit_discrepancy_at1024':str(D1(1024)),'one_bit_discrepancy_at2048':str(D1(2048)),'conclusion':'The saved4096-bit prefix is certified by equal scaled floors. The exact one-bit discrepancy increase disproves monotone doubling for this prefix, not normality.','method':'Reverse-Horner evaluation of rational alternating arctangent partial sums and explicit next-term bounds, followed by Machin interval combination.'}
report={'scope':'Bounded same-workflow review of number_compute.py and output claims6–32, with priority exact checks6,8,23,32. Other output derivations were inspected for obvious scope/arithmetic errors; their computations were not rerun.','confirmed':checks,'corrections':[],'wording_cautions':['In item6 use eventually-descending-in-class only to mean sufficiently large starts descend at step12; the classification is not eventual convergence.','Item23 group fractions should not be confused with finite prime-count proportions; Frobenius assertions exclude odd bad primes and prime2.'],'limits':['No full independent rerun of27 experiments.','No novelty audit or external mathematical endorsement.','The factor() helper has a finite prime table; reviewed call sizes lie within its needed trial-division range, but it is not a general primality/factorization certificate for arbitrary large new inputs.']}
(P/'captain_number_audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps({'confirmed_ids':list(checks),'corrections':[],'collatz_exceptions':exceptions}))
