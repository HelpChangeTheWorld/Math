import json,runpy,cmath,math
from pathlib import Path
p=Path(__file__).parent
# Re-execute source to obtain the numerical functions, preserving all baseline outputs.
ns=runpy.run_path(str(p/'captain_calculations.py'))
data=json.loads((p/'captain_pnp.json').read_text())
checks=0
for name,pairs in [('equality_blocks',[(j,j+4)for j in range(4)]),('four_adjacent_disjunctions',[(2*j,2*j+1)for j in range(4)])]:
 for mask,w in data[name]['residual_width_by_mask'].items():
  mask=int(mask)
  s=sum(((mask>>a)&1)!=((mask>>b)&1)for a,b in pairs)
  c=sum((mask>>a)&1 and (mask>>b)&1 for a,b in pairs)
  assert w==2**s+int(c>0)
  checks+=1
 data[name]['independent_formula']='width=2^s+1_{c>0}; s counts split pairs, c completely assigned pairs.'
(p/'captain_pnp.json').write_text(json.dumps(data,indent=2))
(p/'captain_verification.json').write_text(json.dumps({'exact_pair_formula_checks':checks,'proof':'Every split pair independently imposes one of two different residual conditions. A fully assigned pair additionally allows an inconsistent assignment, producing the zero function. These functions are distinct, yielding 2^s+1_{c>0}. This applies to both equality pairs and disjunction pairs.'},indent=2))
# On the Cauchy sampling circle, direct EM at strongly negative real parts loses digits.
# Reflection of the completed function avoids those cancellations; still not certified.
rawxi=ns['xi']
def reflected_xi(s,N=128,M=10):
 if s.real<.5:return rawxi(1-s,N,M)
 return rawxi(s,N,M)
c=ns['center'];R=ns['radius'];Q=ns['Q'];boundary=ns['boundary']
vals=[reflected_xi(c+R*cmath.exp(2j*math.pi*j/Q))for j in range(Q)]
coeff=[sum(vals[j]*cmath.exp(-2j*math.pi*j*k/Q)for j in range(Q))/Q/R**k for k in range(25)]
def pol(s,d):
 out=0j
 for a in reversed(coeff[:d+1]):out=out*(s-c)+a
 return out
report=json.loads((p/'captain_riemann.json').read_text())
report['direct_circle_em_polynomial_errors']=report.pop('polynomial_sampled_max_errors')
report['reflection_stabilized_polynomial_sampled_errors']={d:max(abs(pol(s,d)-reflected_xi(s))for s in boundary)for d in [8,12,16,24]}
report['numerical_stability_observation']='Reflect xi(s)=xi(1-s) when Re(s)<1/2 during Cauchy-circle evaluation; direct EM there suffers substantial cancellation. The changed residual is a numerical diagnostic, not a certified bound.'
report['interpretation']='A sampled winding near1 and small stabilized sampled polynomial residual do NOT certify a zero count or a Rouche inequality.'
(p/'captain_riemann.json').write_text(json.dumps(report,indent=2))
print('REFINED',json.dumps(report['reflection_stabilized_polynomial_sampled_errors']))
