"""Exact finite calculations and explicitly noncertified complex numerics; stdlib only."""
import cmath, math, json, itertools, collections
from fractions import Fraction as F
from pathlib import Path
OUT=Path(__file__).parent

def write(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2))

# 2: enumerate all orders, using exact set-of-assigned-variables residual tables.
funcs={
 'parity':lambda x:sum(x)%2,
 'equality_blocks':lambda x:int(x[:4]==x[4:]),
 'four_adjacent_disjunctions':lambda x:int(all(x[2*j] or x[2*j+1] for j in range(4)))}
pnp={}
for name,fun in funcs.items():
 widths={}
 for mask in range(256):
  assigned=[j for j in range(8) if mask>>j&1];free=[j for j in range(8) if not(mask>>j&1)]
  residuals=set()
  for a in range(1<<len(assigned)):
   vals=[]
   for b in range(1<<len(free)):
    x=[0]*8
    for k,j in enumerate(assigned):x[j]=(a>>k)&1
    for k,j in enumerate(free):x[j]=(b>>k)&1
    vals.append(fun(x))
   residuals.add(tuple(vals))
  widths[mask]=len(residuals)
 histogram=collections.Counter();cut_ranges=[[999,0] for _ in range(9)];examples={}
 for order in itertools.permutations(range(8)):
  mask=0;w=[widths[0]]
  for j in order:mask|=1<<j;w.append(widths[mask])
  peak=max(w);histogram[peak]+=1;examples.setdefault(peak,{'order':[j+1 for j in order],'widths':w})
  for k,v in enumerate(w):cut_ranges[k][0]=min(cut_ranges[k][0],v);cut_ranges[k][1]=max(cut_ranges[k][1],v)
 assert sum(histogram.values())==math.factorial(8)
 pnp[name]={'orders_checked':40320,'maximum_width_histogram':dict(sorted(histogram.items())),'width_ranges_by_cut':cut_ranges,'witnesses':examples,'residual_width_by_mask':widths}
assert pnp['parity']['maximum_width_histogram']=={2:40320}
write('captain_pnp.json',pnp)

# 3: integer Weierstrass invariants and elementary torsion candidates.
# Nagell-Lutz supplies integral x,y and y=0 or y^2 divides 4A^3+27B^2.
A=-1;B=0;Delta=-16*(4*A**3+27*B**2);c4=-48*A
possible_y=[y for y in range(-2,3) if y==0 or 4%(y*y)==0]
# y^2<=4, x^3-x<0 for x<=-2 and >4 for x>=2.
affine=[(x,y) for x in range(-1,2) for y in possible_y if y*y==x**3-x]
counts={p:1+sum((y*y-x**3+x)%p==0 for x in range(p) for y in range(p)) for p in [3,5,7,11]}
assert affine==[(-1,0),(0,0),(1,0)]
write('captain_bsd.json',{'equation':'y^2=x^3-x','discriminant':Delta,'c4':c4,'j':c4**3//Delta,'bad_prime_candidates':[2], 'nagell_lutz_dependency':'For integral short Weierstrass equations, rational torsion has integral coordinates and y=0 or y^2 divides 4A^3+27B^2.','possible_y':possible_y,'affine_torsion_candidates':affine,'torsion_group':'Z/2 x Z/2, including infinity','point_counts_at_good_primes':counts,'not_computed':['rank','Sha','real period','Tamagawa factors','L-function leading coefficient'],'proof':'Nagell-Lutz bounds |y|<=2 unless y=0. Then -1<=x<=1; direct substitution yields exactly the three displayed y=0 points, each of order2. For y=0 roots are also exactly -1,0,1.'})

# 4: determinant via exact elimination; geometric pairings explained in proof text.
def det(M):
 a=[[F(x) for x in row]for row in M];out=F(1)
 for j in range(len(a)):
  k=next(k for k in range(j,len(a))if a[k][j])
  if k!=j:a[j],a[k]=a[k],a[j];out=-out
  pivot=a[j][j];out*=pivot
  for k in range(j+1,len(a)):
   fac=a[k][j]/pivot
   for l in range(j,len(a)):a[k][l]-=fac*a[j][l]
 return out
M=[[0,1,1,1],[1,0,1,1],[1,1,0,2],[1,1,2,0]]
D=det(M);assert D==-4
write('captain_hodge.json',{'surface':'E x E, E:y^2=x^3-x over C','divisors':['E x {O}','{O} x E','diagonal','graph of i:(x,y)->(-x,iy)'],'intersection_matrix':M,'determinant':str(D),'proof':'Each elliptic divisor has self-intersection0 by adjunction on the abelian surface. Fiber intersections are1. Diagonal intersect graph(i) in ker(i-1), of degree norm(i-1)=2. Nonzero determinant proves four independent rational (1,1) classes. Kunneth gives complex h^(1,1)=1+1+2=4, so they span all rational (1,1) classes. This verifies the established divisor case on this particular surface.'})

# 5: exact Fourier diagonalization of a cycle Laplacian, not a gauge model.
write('captain_gap.json',{'model':'H_(N,a) f(j)=[2f(j)-f(j-1)-f(j+1)]/a^2 on C^N, periodic indices, N>=3','eigenvectors':'v_k(j)=exp(2*pi*i*k*j/N)','eigenvalues':'lambda_k=4*a^(-2)*sin(pi*k/N)^2','gap':'Delta_(N,a)=4*a^(-2)*sin(pi/N)^2>0','limits':{'fixed_a':'Delta tends to0 as N tends to infinity','fixed_L_equals_Na':'Delta tends to4*pi^2/L^2 as N tends to infinity','then_L_to_infinity':'4*pi^2/L^2 tends to0'},'sample_unit_spacing_gaps':{n:4*math.sin(math.pi/n)**2 for n in [4,8,16,32,64]},'proof':'Substitution of v_k into H gives (2-exp(2pi ik/N)-exp(-2pi ik/N))/a^2. The smallest nonzero value occurs at k=1,N-1. The limits follow from sin(x)/x ->1. The eigenvalue identities and limiting conclusion are analytic; displayed decimal samples are illustrative.','scope':'One-particle finite quantum Hamiltonian toy; not Yang-Mills, not a Markov-chain inference, and no continuum gauge theory constructed.'})

# 1: double-precision Euler-Maclaurin zeta + Lanczos gamma, explicitly no certification.
LAN=[0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,-176.61502916214059,12.507343278686905,-0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7]
def gamma(z):
 if z.real<.5:return math.pi/(cmath.sin(math.pi*z)*gamma(1-z))
 z-=1;x=LAN[0]
 for j,a in enumerate(LAN[1:],1):x+=a/(z+j)
 t=z+7.5
 return math.sqrt(2*math.pi)*t**(z+.5)*cmath.exp(-t)*x
BER=[F(1,6),F(-1,30),F(1,42),F(-1,30),F(5,66),F(-691,2730),F(7,6),F(-3617,510),F(43867,798),F(-174611,330)]
def zeta(s,N=64,M=8):
 total=sum(cmath.exp(-s*math.log(n)) for n in range(1,N))
 total+=N**(1-s)/(s-1)+.5*N**(-s)
 rising=1
 for k in range(1,M+1):
  if k==1:rising=s
  else:rising*=(s+2*k-3)*(s+2*k-2)
  total+=float(BER[k-1])/math.factorial(2*k)*rising*N**(-s-2*k+1)
 return total

def xi(s,N=64,M=8):return .5*s*(s-1)*math.pi**(-s/2)*gamma(s/2)*zeta(s,N,M)
center=.5+15j;radius=8.;Q=128
circle=[xi(center+radius*cmath.exp(2j*math.pi*j/Q),128,10)for j in range(Q)]
coeff=[sum(circle[j]*cmath.exp(-2j*math.pi*j*k/Q)for j in range(Q))/Q/radius**k for k in range(25)]
def poly(s,d):
 out=0j
 for c in reversed(coeff[:d+1]):out=out*(s-center)+c
 return out
corners=[0+10j,1+10j,1+20j,0+20j,0+10j]
boundary=[corners[e]+(corners[e+1]-corners[e])*j/128 for e in range(4)for j in range(128)]
v=[xi(s)for s in boundary];v2=[xi(s,128,10)for s in boundary]
wind=sum(cmath.phase(v[(j+1)%len(v)]/v[j])for j in range(len(v)))/(2*math.pi)
num={'status':'NONCERTIFIED floating-point observation only','rectangle':'0<=Re(s)<=1;10<=Im(s)<=20','boundary_samples':len(boundary),'center':[center.real,center.imag],'coefficient_quadrature':{'radius':radius,'samples':Q},'sampled_minimum_abs_xi':min(map(abs,v)),'sampled_winding':wind,'sampled_max_difference_between_em_settings':max(abs(a-b)for a,b in zip(v,v2)), 'polynomial_sampled_max_errors':{d:max(abs(poly(s,d)-value)for s,value in zip(boundary,v2))for d in [8,12,16,24]},'missing_certificate':['uniform Euler-Maclaurin remainder bound','gamma and arithmetic rounding enclosures','Cauchy quadrature/aliasing bound','continuous-boundary nonvanishing and winding enclosure'],'interpretation':'A sampled winding near1 and small sampled polynomial residual do NOT certify a zero count or a Rouche inequality.'}
write('captain_riemann.json',num)
print(json.dumps({'pnp':{k:v['maximum_width_histogram']for k,v in pnp.items()},'torsion':affine,'determinant':str(D),'riemann':num},indent=2))
