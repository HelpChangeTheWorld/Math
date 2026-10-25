#!/usr/bin/env python3
"""Twenty-seven bounded, exact number-theory work attempts.

Standard library only. Each number_<id>.json is written immediately.
These are finite calibrations or elementary restricted arguments, not solutions
of the unrestricted conjectures. Run this file from any working directory.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, factorial, gcd, isqrt, lcm
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(0)
OUT = Path(__file__).resolve().parent


def frac(x):
    x = F(x)
    return f'{x.numerator}/{x.denominator}'


def enclosure(lo, hi, digits=18):
    scale = 10 ** digits
    a = (lo * scale).__floor__()
    b = (hi * scale).__ceil__()
    return {'lower': frac(F(a, scale)), 'upper': frac(F(b, scale))}


def emit(i, result):
    (OUT / f'number_{i}.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f'Completed item {i}', flush=True)


LIMIT = 4_010_000
prime = bytearray(b'\x01') * (LIMIT + 1)
prime[:2] = b'\x00\x00'
for p in range(2, isqrt(LIMIT) + 1):
    if prime[p]:
        prime[p*p:LIMIT+1:p] = b'\x00' * ((LIMIT-p*p)//p+1)
PRIMES = [n for n in range(2, LIMIT+1) if prime[n]]


def factor(n):
    out = {}
    for p in PRIMES:
        if p*p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def isprime(n):
    if n <= LIMIT:
        return n >= 2 and bool(prime[n])
    return len(factor(n)) == 1 and next(iter(factor(n).values())) == 1


def sigma(n):
    r = 1
    for p, e in factor(n).items():
        r *= (p**(e+1)-1)//(p-1)
    return r


def phi(n):
    r = n
    for p in factor(n):
        r = r//p*(p-1)
    return r


def log_unit_bounds(u, terms=32):
    t = (u-1)/(u+1)
    assert 0 <= t <= F(1, 3)
    power, low = t, F(0)
    for j in range(terms):
        low += 2*power/(2*j+1)
        power *= t*t
    tail = 2*power/((2*terms+1)*(1-t*t))
    return low, low+tail


LOG2 = log_unit_bounds(F(2))


@lru_cache(None)
def log_bounds(n):
    k = n.bit_length()-1
    lo, hi = log_unit_bounds(F(n, 2**k))
    return lo+k*LOG2[0], hi+k*LOG2[1]


def atan_bounds(q, terms):
    power, s = F(1,q), F(0)
    for j in range(terms):
        s += (-1 if j % 2 else 1)*power/(2*j+1)
        power /= q*q
    nxt = (-1 if terms % 2 else 1)*power/(2*terms+1)
    return min(s,s+nxt), max(s,s+nxt)


def pi_bounds(a_terms=70, b_terms=25):
    a, b = atan_bounds(5,a_terms), atan_bounds(239,b_terms)
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


def positive_product(a,b):
    assert a[0]>=0 and b[0]>=0
    return a[0]*b[0], a[1]*b[1]


# 6: full, prescribed residue computation for the one-division map S.
def shortcut(n):
    return n//2 if n%2==0 else (3*n+1)//2


rows=[]
for r in range(4096):
    n = r or 4096
    A,B,den=1,0,1
    bits=[]
    v=n
    for _ in range(12):
        odd=v%2
        bits.append(odd)
        if odd:
            A,B=3*A,3*B+den
        den*=2
        v=shortcut(v)
    for start in [n,n+4096,n+8192]:
        v=start
        for _ in range(12):
            v=shortcut(v)
        assert den*v == A*start+B
    D=den-A
    threshold=B//D+1 if D>0 else None
    exceptions=[]
    if threshold is not None:
        exceptions=list(range(n,threshold,4096))
    rows.append({'r':r,'odd_steps':sum(bits),'A':A,'B':B,
                 'parity_word':bits,'D':D,'minimum_integer_for_descent':threshold,
                 'finite_non_descending_representatives':exceptions})
emit(6, {'map':'S(n)=n/2 if n even; (3n+1)/2 if n odd',
         'modulus':4096,'steps':12,'affine_checks':4096*3,
         'eventually_descending_classes':sum(t['D']>0 for t in rows),
         'never_descending_at_step_12_classes':sum(t['D']<=0 for t in rows),
         'finite_exceptions_in_contracting_classes':sum(len(t['finite_non_descending_representatives']) for t in rows),
         'largest_threshold':max(t['minimum_integer_for_descent'] or 0 for t in rows),
         'rows':rows})

# 7: reduced exact Goldbach census, with ordered normalization.
counts=[]
for N in range(4,2001,2):
    R=sum(prime[p] and prime[N-p] for p in range(2,N-1))
    counts.append({'N':N,'ordered_representations':R})
assert counts[0]['ordered_representations']==1
examples=[]
for N in [1000,1002,1010,1260,1998,2000]:
    factors={}
    for y in [7,31]:
        c=F(1)
        for ell in PRIMES:
            if ell>y: break
            nu=1 if N%ell==0 else 2
            c*=F(1)-F(nu,ell)
            c/=(F(1)-F(1,ell))**2
        factors[str(y)]=frac(c)
    examples.append({'N':N,'ordered_count':counts[(N-4)//2]['ordered_representations'],
                     'truncated_local_factors':factors})
emit(7, {'cutoff':2000,'tested_even_integers':len(counts),
         'zero_counts':[t for t in counts if t['ordered_representations']==0],
         'minimum_count_for_N_at_least_1000':min(t['ordered_representations'] for t in counts if t['N']>=1000),
         'local_factor_examples':examples,'counts':counts,
         'not_computed':'Logarithmic integral baselines, smoothing, and asymptotic error estimates.'})

# Shared exact Liouville / Möbius data.
SMALL=100020
spf=list(range(SMALL+1))
for p in range(2,isqrt(SMALL)+1):
    if spf[p]==p:
        for n in range(p*p,SMALL+1,p):
            if spf[n]==n: spf[n]=p
omega=[0]*(SMALL+1)
mu=[1]*(101)
for n in range(2,SMALL+1):
    omega[n]=omega[n//spf[n]]+1
for d in range(2,101):
    fac=factor(d)
    mu[d]=0 if any(e>1 for e in fac.values()) else (-1)**len(fac)

# 8: all six exact weights on both specified intervals.
weight_results=[]
for R in [30,100]:
    coef={j:[mu[d]*(R-d)**j for d in range(1,R+1)] for j in [1,2,3]}
    windows=[defaultdict(int),defaultdict(int)]
    bins=[defaultdict(Counter),defaultdict(Counter)]
    for n in range(2,40001):
        widx=0 if n<=20000 else 1
        divs=[d for d in range(1,R+1) if n*(n+2)%d==0]
        pair=bool(prime[n] and prime[n+2])
        om=omega[n]+omega[n+2]
        for j in [1,2,3]:
            numerator=sum(coef[j][d-1] for d in divs)**2
            windows[widx][('total',j)]+=numerator
            windows[widx][('pair',j)]+=numerator*pair
            bins[widx][j][om]+=numerator
    for j in [1,2,3]:
        for wi,(lo,hi) in enumerate([(2,20000),(20001,40000)]):
            total=windows[wi][('total',j)]
            pmass=windows[wi][('pair',j)]
            weight_results.append({'R':R,'j':j,'lo':lo,'hi':hi,
                'denominator':R**(2*j),'total_numerator':total,'prime_pair_numerator':pmass,
                'normalized_prime_pair_mass':frac(F(pmass,total)),
                'omega_mass_numerators':dict(sorted(bins[wi][j].items()))})
baselines=[]
for lo,hi in [(2,20000),(20001,40000)]:
    pairs=sum(prime[n] and prime[n+2] for n in range(lo,hi+1))
    sift=[n for n in range(lo,hi+1) if gcd(n*(n+2),30)==1]
    siftpairs=sum(prime[n] and prime[n+2] for n in sift)
    baselines.append({'lo':lo,'hi':hi,'pairs':pairs,
        'unweighted_fraction':frac(F(pairs,hi-lo+1)),
        'wheel_survivors':len(sift),'wheel_prime_pairs':siftpairs,
        'wheel_fraction':frac(F(siftpairs,len(sift)))})
emit(8, {'formula':'W_j(n;R)=(sum_{d<=R,d|n(n+2)} mu(d)*(1-d/R)^j)^2',
         'arithmetic':'Exact integer numerators with common denominator R^(2j).',
         'configurations':weight_results,'baselines':baselines})

# 9: exact polynomial normalizations and an explicit prime-power correction.
kernels=[]
for j in [2,3,4]:
    c=F(factorial(2*j+1),factorial(j)**2)
    coeff={j+k:c*comb(j,k)*(-1)**k for k in range(j+1)}
    integral=sum(v/F(k+1) for k,v in coeff.items())
    assert integral==1
    deriv={k-1:k*v for k,v in coeff.items()}
    energy=sum(v*w/F(k+ell+1) for k,v in deriv.items() for ell,w in deriv.items())
    t=F(2,11)
    kernels.append({'j':j,'normalizer':frac(c),'integral':frac(integral),
                    'derivative_L2_squared':frac(energy),
                    'weight_at_m27_in_n5_interval':frac(c*(t*(1-t))**j)})
interval_counts=[sum(prime[m] for m in range(n*n+1,(n+1)**2)) for n in range(1,201)]
emit(9, {'intervals_checked':200,'empty_intervals':sum(c==0 for c in interval_counts),
         'kernels':kernels,'prime_power_witness':{'n':5,'interval':[25,36],'m':27,'base_prime':3,
         'correction':'At m=27 the von Mangoldt sum includes log(3)*w_j(2/11), while the prime-only sum does not.'}})

# 10: reduced Gaussian-line calibration with exact local root counts.
lines=[]
for b in [1,2,3,4,8]:
    good=[n for n in range(1,2001) if prime[n*n+b*b]]
    forced=[n for n in range(1,2001) if gcd(n,b)>1]
    assert not any(prime[n*n+b*b] for n in forced)
    lines.append({'b':b,'prime_norm_count':len(good),'first_prime_inputs':good[:10],
                  'gcd_forced_composites':len(forced),
                  'roots_mod_small_primes':{str(p):sum((x*x+b*b)%p==0 for x in range(p))
                                           for p in PRIMES if p<=31}})
emit(10, {'n_cutoff':2000,'lines':lines,'not_computed':'No strip-to-line uniform error estimate.'})

# 11: Lucas--Lehmer versus a deliberately bounded trial sieve.
mersenne=[]
for p in [q for q in PRIMES if q<=127]:
    M=2**p-1
    s=4
    if p==2:
        passes=True
    else:
        for _ in range(p-2): s=(s*s-2)%M
        passes=s==0
    divisors=[q for q in PRIMES if q<=1000 and q<M and pow(2,p,q)==1]
    mersenne.append({'p':p,'lucas_lehmer_prime':passes,'proper_prime_factors_at_most_1000':divisors})
emit(11, {'prime_exponent_cutoff':127,'trial_factor_cutoff':1000,'rows':mersenne,
          'composite_trial_survivors':[t['p'] for t in mersenne if not t['lucas_lehmer_prime'] and not t['proper_prime_factors_at_most_1000']]})

# 12: a sound local branch-pruning certificate and a short factor chain.
d=3**2*5**2*7**2
assert sigma(d)>2*d
chain=[]
for p in [3,13,61,97]:
    s=(p**3-1)//(p-1)
    chain.append({'assumed_prime_power':[p,2],'sigma':s,'factorization':factor(s)})
emit(12, {'forced_divisor':d,'sigma_d':sigma(d),'twice_d':2*d,'abundancy':frac(F(sigma(d),d)),
          'lemma':'If d divides N then sigma(N)/N >= sigma(d)/d. Therefore 11025 dividing N excludes perfection.',
          'conditional_chain':chain,'limit':'The listed exponent-two choices are assumptions; alternative exponents and the Euler special prime remain unresolved.'})

# 13: explicit local-survival obstruction for every proposed exponent triple.
moduli=[16,27,25,7,11,13]
M=lcm(*moduli)
A,B,C=M,M+1,2*M+1
assert gcd(A,B)==gcd(A,C)==gcd(B,C)==1
checks=0
for x,y,z in product(range(3,8),repeat=3):
    for modulus in moduli:
        assert (pow(A,x,modulus)+pow(B,y,modulus)-pow(C,z,modulus))%modulus==0
        checks+=1
emit(13, {'moduli':moduli,'M':M,'primitive_bases':[A,B,C],'congruence_checks':checks,
          'cubic_integer_residual':A**3+B**3-C**3,
          'lemma':'For any finite moduli, A=M,B=M+1,C=2M+1 are pairwise coprime and satisfy A^x+B^y=C^z modulo every modulus for all positive exponents. Thus these congruences alone cannot eliminate an entire exponent triple.'})

# 14: prove the k=1 and k=2 subcases algebraically, with exact checks.
for m in range(2,101):
    assert 6*(sum(j*j for j in range(1,m))-m*m)==m*(2*m*m-9*m+1)
assert 8**2<73<9**2
emit(14, {'k1_reduction':'m(m-3)=0; m>=2 gives m=3, namely 1+2=3.',
          'k2_identity':'6*(sum_{j=1}^{m-1}j^2-m^2)=m*(2m^2-9m+1)',
          'k2_discriminant':73,'between_consecutive_squares':[64,81],
          'conclusion':'No positive integer m>=2 solves the k=2 equation.',
          'independent_identity_checks':99,'scope':'Only k=1 and k=2; no uniform argument in k.'})

# 15: reduced, fully factored polynomial-prime/control comparison.
polynomials=[('x^2+1',lambda x:x*x+1),('x^2+x+41',lambda x:x*x+x+41),
             ('x^3+2',lambda x:x**3+2),('(x+1)(x+2)',lambda x:(x+1)*(x+2)),
             ('(x+1)(x^2+1)',lambda x:(x+1)*(x*x+1))]
poly_rows=[]
for name,f in polynomials:
    prime_count=0
    survivor_count=0
    omega_counts=Counter()
    for n in range(1,1001):
        fac=factor(f(n))
        om=sum(fac.values())
        prime_count+=om==1
        survivor_count+=min(fac)>31
        omega_counts[om]+=1
    poly_rows.append({'polynomial':name,'prime_count':prime_count,
        'all_prime_factors_greater_than_31':survivor_count,'omega_histogram':dict(omega_counts),
        'local_root_counts':{str(p):sum(f(x)%p==0 for x in range(p)) for p in PRIMES if p<=31}})
emit(15, {'input_cutoff':1000,'rows':poly_rows,
          'irreducibility_certificates':['x^2+1 has discriminant -4.','x^2+x+41 has discriminant -163.',
            'The only rational-root candidates of monic x^3+2 are +/-1,+/-2; none is a root.'],
          'control_limit':'The reducible controls were not matched to all local root counts; classification differences are not evidence of a new prime detector.'})

# 16: all ten polynomial-pair local products and finite prime counts.
bh=[]
for a in [4+6*j for j in range(10)]:
    cs={}
    for y in [31,101]:
        c=F(1)
        for ell in PRIMES:
            if ell>y: break
            nu=sum(t*(t*t+a)%ell==0 for t in range(ell))
            assert nu<ell
            c*=F(1)-F(nu,ell)
            c/=(F(1)-F(1,ell))**2
        cs[str(y)]=frac(c)
    count=sum(prime[n] and prime[n*n+a] for n in range(2,1001))
    bh.append({'a':a,'joint_primes_through_1000':count,'C31':cs['31'],'C101':cs['101'],
               'C101_div_C31':frac(F(cs['101'])/F(cs['31']))})
emit(16, {'pairs':'n and n^2+a, a=4+6j for 0<=j<=9','rows':bh,
          'admissibility_proof':'Modulo 2 and 3, a=4 mod 6 leaves allowed inputs. For every prime ell>=5, the nonzero degree-three polynomial t(t^2+a) has at most three roots, fewer than ell.',
          'limit':'No Euler-product tail estimate or logarithmic integral was computed; these are truncated local products, not fitted asymptotic predictions.'})

# 17: exact order-index audit on a reduced prime range.
orders=[]
for g in [2,3,5,1,4]:
    primitive=0
    missed=[]
    considered=0
    obstruction_counts=Counter()
    for p in PRIMES:
        if p>10000: break
        if p==2 or g%p==0: continue
        considered+=1
        order=p-1
        for ell in factor(p-1):
            while order%ell==0 and pow(g,order//ell,p)==1:
                order//=ell
        assert pow(g,order,p)==1
        assert all(pow(g,order//ell,p)!=1 for ell in factor(order))
        index=(p-1)//order
        primitive+=index==1
        obs=[ell for ell in [2,3,5,7,11,13] if index%ell==0]
        for ell in obs: obstruction_counts[ell]+=1
        if index>1 and not obs:
            missed.append({'p':p,'order':order,'index':index})
    if g in [1,4]: assert primitive==0
    orders.append({'g':g,'odd_good_primes':considered,'primitive_root_count':primitive,
                   'small_index_obstruction_counts':dict(obstruction_counts),
                   'large_index_only_failures':missed})
emit(17, {'prime_cutoff':10000,'rows':orders,'limit':'Finite index tails only; no independence or uniform tail estimate.'})

# 18: rigorously enclosed reduced EH error sum, x=100.
x=100
prime_power={}
for p in PRIMES:
    if p>x: break
    n=p
    while n<=x:
        prime_power[n]=p
        n*=p


def abs_bounds(lo,hi):
    if lo<=0<=hi: return F(0),max(-lo,hi)
    return min(abs(lo),abs(hi)),max(abs(lo),abs(hi))


eh=[]
band_totals=defaultdict(lambda:[F(0),F(0)])
for q in range(1,101):
    if q**10>x**7: continue
    arows=[]
    coeffsum=Counter()
    for a in range(q):
        if gcd(a,q)!=1: continue
        coeff=Counter(p for n,p in prime_power.items() if n%q==a)
        coeffsum.update(coeff)
        lo=sum((mult*log_bounds(p)[0] for p,mult in coeff.items()),F(0))-F(x,phi(q))
        hi=sum((mult*log_bounds(p)[1] for p,mult in coeff.items()),F(0))-F(x,phi(q))
        arows.append(abs_bounds(lo,hi))
    assert coeffsum==Counter(p for n,p in prime_power.items() if gcd(n,q)==1)
    lo,hi=max(t[0] for t in arows),max(t[1] for t in arows)
    largest=max(factor(q),default=1)
    band='q=1' if q==1 else 'Pplus<=13' if largest<=13 else '13<Pplus<=sqrt(q)' if largest*largest<=q else 'Pplus>max(13,sqrt(q))'
    band_totals[band][0]+=lo
    band_totals[band][1]+=hi
    eh.append({'q':q,'band':band,'max_error':enclosure(lo,hi)})
emit(18, {'x':x,'theta':'7/10','q_max':max(t['q'] for t in eh),'moduli':eh,
          'band_totals':{k:enclosure(*v) for k,v in band_totals.items()},
          'exact_accounting_checks':len(eh),
          'log_bound_method':'Range reduction and 32-term positive arctanh series with explicit geometric tail; final rational intervals rounded outward.',
          'limit':'A finite x=100 diagnostic, not the proposed larger range or an asymptotic dispersion estimate.'})

# 19: two-point Liouville correlations, full and small-prime-stripped.
liouville=[(-1)**o for o in omega]
rough_sign=[1]*(SMALL+1)
for n in range(1,SMALL+1):
    m=n
    small_omega=0
    for p in [2,3,5,7]:
        while m%p==0:
            m//=p
            small_omega+=1
    rough_sign[n]=liouville[m]
    assert liouville[n]==(-1)**small_omega*rough_sign[n]
corr=[]
for X in [1000,10000,100000]:
    for h in range(1,21):
        original_sum=sum(liouville[n]*liouville[n+h] for n in range(1,X+1))
        stripped_sum=sum(rough_sign[n]*rough_sign[n+h] for n in range(1,X+1))
        corr.append({'X':X,'h':h,'liouville_sum':original_sum,'rough_sum':stripped_sum})
assert sum(liouville[n]**2 for n in range(1,100001))==100000
counter=next(t for t in corr if abs(t['rough_sum'])>abs(t['liouville_sum']))
emit(19, {'rows':corr,'h0_control_at_100000':100000,
          'counterexample_to_monotonic_bias_reduction':counter,
          'limit':'These are unweighted two-point finite sums, not an estimate for all orders or all scales.'})

# 20: exact triangular-peak obstruction to moment-only pointwise control.
peaks=[]
for H in [2,4,8]:
    D=H**3
    moment=F(2*H**3,3*D)
    assert moment==F(2,3)
    peaks.append({'height':H,'slope_bound':D,'half_support_width':frac(F(H,D)),
                  'integral_F_squared':frac(moment)})
emit(20, {'family':'F_H(t)=max(H-H^3*abs(t),0)', 'rows':peaks,
          'general_identity':'For F(t)=max(H-D|t|,0), integral_R F(t)^(2k)dt = 2H^(2k+1)/(D(2k+1)).',
          'conclusion':'Uniform second-moment control permits arbitrarily high peaks when the derivative bound is allowed to grow with height.',
          'limit':'A proved elementary function-family obstruction, not a construction of zeta peaks or a zeta derivative estimate.'})

# 21: actual first 200 primes and height-bounded smooth sets.
candidates=[p for p in PRIMES if p>=10000][:200]
small_primes=[2,3,5,7,11,13]
patterns=[]
compatible=[]
for p in candidates:
    chars=[1 if pow(ell,(p-1)//2,p)==1 else -1 for ell in small_primes]
    patterns.append({'p':p,'characters':chars})
    if all(c==1 for c in chars):
        smooth=[]
        for n in range(1,p):
            m=n
            for ell in small_primes:
                while m%ell==0: m//=ell
            if m==1: smooth.append(n)
        vals=[1 if pow(n,(p-1)//2,p)==1 else -1 for n in smooth]
        assert sum(vals)==len(smooth)
        compatible.append({'p':p,'smooth_count':len(smooth),'character_sum':sum(vals),
                           'height':p-1})
residues=sorted({n*n%17 for n in range(1,17)})
sumset=sorted({(a+b)%17 for a in residues for b in residues})
assert sumset==list(range(17))
emit(21, {'first_prime':candidates[0],'last_prime':candidates[-1],'primes_tested':len(candidates),
          'patterns':patterns,'compatible_cases':compatible,
          'negative_control_mod17':{'residues':residues,'sumset':sumset},
          'conclusion':'Compatibility forces the smooth-set character sum to equal its size. Additive growth alone supplies no contradictory cancellation estimate.'})

# 22: independent q-product coefficients, Hecke recurrence, and congruence.
N=200
coeff=[0]*N
coeff[0]=1
for m in range(1,N):
    old=coeff
    new=old.copy()
    for j in range(1,min(24,(N-1)//m)+1):
        c=(-1)**j*comb(24,j)
        shift=m*j
        for k in range(shift,N): new[k]+=c*old[k-shift]
    coeff=new
tau=[0]+coeff
s11=[0]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d): s11[n]+=d**11
assert all((tau[n]-s11[n])%691==0 for n in range(1,N+1))
hecke=0
for p in PRIMES:
    if p*p>N: break
    prev,current=1,p
    while current*p<=N:
        assert tau[current*p]==tau[p]*tau[current]-p**11*tau[prev]
        hecke+=1
        prev,current=current,current*p
assert (tau[1],tau[2],tau[4])==(1,-24,-1472)
survivors=[p for p in PRIMES if p<=10000 and (1+pow(p,11,691))%691==0]
assert gcd(11,690)==1 and all(p%691==690 for p in survivors)
emit(22, {'coefficient_cutoff':N,'tau_values':tau[1:],'zero_coefficients':[n for n in range(1,N+1) if tau[n]==0],
          'hecke_checks':hecke,'congruence_checks':N,
          'prime_zero_filter_survivors_through_10000':survivors,
          'necessary_condition':'A hypothetical prime zero must satisfy p=-1 mod 691, since gcd(11,690)=1.',
          'limit':'Surviving congruences are necessary conditions only; no universal nonvanishing claim.'})

# 23: new mod-2 Galois-image calculation; no repeat point counts.
gl2=[]
stabilizer=[]
for a,b,c,d in product(range(2),repeat=4):
    if (a*d-b*c)%2==1:
        row={'matrix':[[a,b],[c,d]],'trace_mod_2':(a+d)%2}
        gl2.append(row)
        if a==1 and c==0: stabilizer.append(row)
assert len(gl2)==6 and len(stabilizer)==2
assert all(t['trace_mod_2']==0 for t in stabilizer)
assert all(n**3-n+1!=0 for n in [-1,1])
emit(23, {'E1_cubic':'x^3-x+1','E1_irreducibility':'Monic cubic with constant 1: rational-root candidates +/-1 both fail.',
          'E1_cubic_discriminant':-23,
          'E1_galois_image_proof':'Irreducible cubic with nonsquare discriminant has Galois group S3; permutation of nonzero two-torsion identifies this with GL2(F2).',
          'E1_group':gl2,'E1_trace_one_fraction':frac(F(sum(t['trace_mod_2']==1 for t in gl2),len(gl2))),
          'E2_cubic_factorization':'(x-1)(x^2+x-1)','E2_quadratic_discriminant':5,
          'E2_galois_image_proof':'The quadratic factor splits over Q(sqrt(5)); the rational root is fixed, giving the order-two stabilizer of a nonzero two-torsion vector.',
          'E2_group':stabilizer,'E2_trace_one_fraction':'0/1',
          'limit':'Only modulus 2 is certified. No modulus-3 image, modulus-6 entanglement, or growing-resolution asymptotic was obtained.'})

# 24: genuine rank-one p-adic unit-log calibration in Q(sqrt(5)).
p=11
root=next(r for r in range(4,121,11) if (r*r-5)%121==0)
epsilon=(1+root)*pow(2,-1,121)%121
unit_power=pow(epsilon,10,121)
assert root==48 and epsilon==85 and unit_power==111
assert (epsilon*epsilon-epsilon-1)%121==0
emit(24, {'field':'Q(sqrt(5))','unit':'epsilon=(1+sqrt(5))/2, norm -1','split_prime':11,
          'sqrt5_mod_121':root,'epsilon_mod_121':epsilon,'epsilon_power10_mod_121':unit_power,
          'valuation_log_epsilon':1,
          'proof':'epsilon^10=1+110 mod 121, so v_11(epsilon^10-1)=1. In log(1+u), every term after u has valuation at least 2. Thus log(epsilon^10), and hence log(epsilon), has valuation 1 and is nonzero.',
          'conclusion':'This explicit unit certifies a nonzero rank-one logarithm in the quadratic calibration field.',
          'limit':'An established quadratic case, not the planned five cubic fields or a general Leopoldt proof.'})

# 25: two certified algebraic measures from the proposed coefficient family.
glo,ghi=F(1618033,10**6),F(1618034,10**6)
assert (2*glo-1)**2<5<(2*ghi-1)**2
plo,phi_=F(1324717,10**6),F(1324718,10**6)
f=lambda t:t**3-t-1
assert f(plo)<0<f(phi_)
assert phi_<F(7,5)
emit(25, {'quadratic':{'polynomial':'x^2-x-1','measure_interval':[frac(glo),frac(ghi)],
                     'reason':'Roots are (1+sqrt(5))/2 and (1-sqrt(5))/2; only the first has absolute value above one.'},
          'cubic':{'polynomial':'x^3-x-1','measure_interval':[frac(plo),frac(phi_)],
                   'endpoint_polynomial_values':[frac(f(plo)),frac(f(phi_))],
                   'reason':'No rational root; discriminant -23 gives one real root rho>1. The other two roots are conjugate with squared modulus 1/rho<1, so Mahler measure equals rho.'},
          'conclusion':'The cubic measure is rigorously below 7/5. Any attempted universal lower bound of 1.4 is incompatible with this known example.',
          'limit':'Two explicit examples only; no enumeration minimum or degree-independent lower bound.'})

# 26: complete prescribed 16-prime subset census.
base_primes=[3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
ns=[1]*(1<<16)
phis=[1]*(1<<16)
hits=[]
closest=None
for mask in range(1<<16):
    if mask:
        bit=mask & -mask
        idx=bit.bit_length()-1
        prev=mask^bit
        ns[mask]=ns[prev]*base_primes[idx]
        phis[mask]=phis[prev]*(base_primes[idx]-1)
    n,t=ns[mask],phis[mask]
    r=(n-1)%t
    if r==0: hits.append({'mask':mask,'n':n,'phi':t,'prime_factors':mask.bit_count()})
    if mask.bit_count()>=2:
        distance=F(min(r,t-r),t)
        if closest is None or distance<closest[0]:
            closest=(distance,{'mask':mask,'n':n,'phi':t,'remainder':r,'distance_to_integer':frac(distance)})
assert len(hits)==17 and all(t['prime_factors']<=1 for t in hits)
emit(26, {'base_primes':base_primes,'subsets_checked':1<<16,'composite_subsets_checked':(1<<16)-17,
          'divisibility_hits':hits,'closest_composite_ratio_to_integer':closest[1],
          'limit':'Complete only for subsets of these sixteen primes. No pruning rule or unrestricted exclusion is proved.'})

# 27: complete inverse-totient recursion for values <=100.
def divisors(n):
    ans=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            ans.append(d)
            if d*d!=n: ans.append(n//d)
    return sorted(ans)


@lru_cache(None)
def inverse_phi(rem,min_prime=2):
    answers={1} if rem==1 else set()
    for d in divisors(rem):
        p=d+1
        if p<min_prime or not isprime(p): continue
        cost=p-1
        ppow=p
        while rem%cost==0:
            for tail in inverse_phi(rem//cost,p+1):
                answers.add(ppow*tail)
            cost*=p
            ppow*=p
    return tuple(sorted(answers))


inverses={str(v):list(inverse_phi(v)) for v in range(1,101)}
for v,preimages in inverses.items():
    assert all(phi(n)==int(v) for n in preimages)
assert inverses['1']==[1,2] and inverses['8']==[15,16,20,24,30]
singleton=[int(v) for v,pre in inverses.items() if len(pre)==1]
emit(27, {'totient_cutoff':100,'all_preimages':inverses,'realized_values':sum(bool(t) for t in inverses.values()),
          'singleton_values':singleton,'largest_preimage':max(n for pre in inverses.values() for n in pre),
          'completeness_argument':'Every unused prime p contributes p^(e-1)(p-1), dividing the remaining totient factor. Enumerating divisors d and p=d+1 therefore lists every next prime. Increasing p prevents repetition; p=2 with cost 1 is handled without premature termination.',
          'limit':'Complete bounded-value calculation only; no partner construction for arbitrary integers.'})

# 28: exact witnesses, searching coprime numerators until the first success.
def continued_fraction(a,q):
    digits=[]
    while a:
        b,r=divmod(q,a)
        digits.append(b)
        q,a=a,r
    return digits


def representations(a,q):
    digits=continued_fraction(a,q)
    return [digits,digits[:-1]+[digits[-1]-1,1]]


zaremba=[]
missing_A2=[]
for q in range(2,2001):
    found=None
    has_A2=False
    for a in range(1,q):
        if gcd(a,q)!=1: continue
        reps=representations(a,q)
        if q<=200 and any(max(ds)<=2 for ds in reps): has_A2=True
        if found is None:
            good=[ds for ds in reps if max(ds)<=5]
            if good:
                ds=min(good,key=lambda z:(len(z),z))
                num_prev,num=1,0
                den_prev,den=0,1
                for b in ds:
                    num_prev,num=num,b*num+num_prev
                    den_prev,den=den,b*den+den_prev
                assert (num,den)==(a,q)
                found={'q':q,'a':a,'digits':ds}
        if q>200 and found is not None: break
    if q<=200 and not has_A2: missing_A2.append(q)
    assert found is not None
    zaremba.append(found)
emit(28, {'denominator_cutoff':2000,'witness_count':len(zaremba),'witnesses':zaremba,
          'A2_missing_denominators_through_200':missing_A2,
          'convention':'Both finite continued-fraction representations are permitted, including a final digit 1.',
          'limit':'Finite witness census, not a universal construction or a proof for all denominators.'})

# 29: exact rational interval exclusion of a complete finite polynomial family.
eterms=80
elo=sum((F(1,factorial(k)) for k in range(eterms+1)),F(0))
ehi=elo+F(1,factorial(eterms)*eterms)
epi=(elo,ehi)
pip=pi_bounds()
monomials=[(F(1),F(1)),epi,pip,positive_product(epi,epi),positive_product(epi,pip),positive_product(pip,pip)]
den=lcm(*(v.denominator for interval in monomials for v in interval))
mbounds=[(int(lo*den),int(hi*den)) for lo,hi in monomials]
tested=0
unresolved=[]
best=None
for coeffs in product(range(-2,3),repeat=6):
    if not any(coeffs): continue
    first=next(c for c in coeffs if c)
    if first<0 or gcd(*coeffs)!=1: continue
    tested+=1
    lo=sum(c*(a if c>=0 else b) for c,(a,b) in zip(coeffs,mbounds))
    hi=sum(c*(b if c>=0 else a) for c,(a,b) in zip(coeffs,mbounds))
    if lo<=0<=hi:
        unresolved.append(coeffs)
    else:
        separation=min(abs(lo),abs(hi))
        if best is None or separation<best[0]: best=(separation,coeffs,lo,hi)
assert not unresolved
emit(29, {'basis':['1','e','pi','e^2','e*pi','pi^2'],'coefficient_set':[-2,-1,0,1,2],
          'normalization':'gcd of coefficients one; first nonzero coefficient positive.',
          'canonical_polynomials_tested':tested,'unresolved':unresolved,
          'smallest_certified_separation_example':{'coefficients':best[1],'evaluation':enclosure(F(best[2],den),F(best[3],den))},
          'certification':'e: 80-term factorial sum and positive tail bound. pi: Machin formula with 70 and 25 arctangent terms and alternating-series error bounds. All polynomial interval arithmetic is rational.',
          'limit':'A finite family only; no algebraic independence or Schanuel conclusion.'})

# 30: exact multiplicative-independence filter plus determinant intervals.
small=list(range(2,11))
profiles={n:[factor(n).get(p,0) for p in [2,3,5,7]] for n in small}
def independent(a,b):
    u,v=profiles[a],profiles[b]
    return any(u[i]*v[j]!=u[j]*v[i] for i in range(4) for j in range(4))


products={(a,b):positive_product(log_bounds(a),log_bounds(b)) for a,b in product(small,repeat=2)}
den=lcm(*(v.denominator for interval in products.values() for v in interval))
prodints={k:(int(v[0]*den),int(v[1]*den)) for k,v in products.items()}
tested=0
unresolved=[]
best=None
for a,b,c,d in product(small,repeat=4):
    if not independent(a,b) or not independent(a,c): continue
    tested+=1
    first,second=prodints[a,d],prodints[b,c]
    lo,hi=first[0]-second[1],first[1]-second[0]
    if lo<=0<=hi: unresolved.append([a,b,c,d])
    else:
        separation=min(abs(lo),abs(hi))
        if best is None or separation<best[0]: best=(separation,[a,b,c,d],lo,hi)
assert not unresolved and not independent(2,4)
emit(30, {'integer_range':[2,10],'retained_quadruples':tested,'unresolved':unresolved,
          'smallest_separation_example':{'a_b_c_d':best[1],'determinant':enclosure(F(best[2],den),F(best[3],den))},
          'exact_zero_excluded_control':{'a_b_c_d':[2,4,3,9],'identity':'log(2)*2log(3)-2log(2)*log(3)=0','reason':'2 and 4 are multiplicatively dependent.'},
          'certification':'Prime-exponent vectors test independence exactly; rational arctanh-series enclosures certify logarithmic determinants.',
          'limit':'Only integers 2 through 10, not the original cutoff 30 or all algebraic logarithms.'})

# 31: proved elementary harmonic-remainder bounds and denominator ledger.
harmonic=F(0)
D=1
ledger=[]
for n in range(1,13):
    harmonic+=F(1,n)
    D=lcm(D,n)
    assert (D*harmonic).denominator==1
    ledger.append({'n':n,'harmonic':frac(harmonic),'lcm_denominator':D,
                   'cleared_remainder_lower':frac(F(D,2*(n+1))),
                   'cleared_remainder_upper':frac(F(D,2*n))})
emit(31, {'ledger':ledger,
          'remainder_identity':'H_n-log(n)-gamma=sum_{k=n}^infinity [log(1+1/k)-1/(k+1)].',
          'bound_proof':'Each summand equals integral_0^1 (1-t)/[(k+t)(k+1)] dt, between 1/[2(k+1)^2] and 1/[2k(k+1)]. Summing and comparing with an integral gives 1/[2(n+1)] <= remainder <= 1/(2n).',
          'obstruction':'Clearing harmonic denominators leaves the logarithmic term D_n log(n); the resulting expression is not an integer linear form in gamma. At n=12 its cleared remainder is already greater than 1000.',
          'limit':'An exact calibration of the naive harmonic approximation, not the unselected integral construction or an irrationality proof.'})

# 32: certified first 4096 binary digits of pi, then a specified monotonicity test.
N=4096
pi_lo,pi_hi=pi_bounds(1000,300)
digit_lo=((pi_lo-3)*2**N).__floor__()
digit_hi=((pi_hi-3)*2**N).__floor__()
assert digit_lo==digit_hi
bits=f'{digit_lo:0{N}b}'
discrepancies=[]
values={}
for size in [256,512,1024,2048,4096]:
    for k in range(1,9):
        counts=Counter(bits[i:i+k] for i in range(size-k+1))
        total=size-k+1
        Dk=max(abs(F(counts[f'{word:0{k}b}'],total)-F(1,2**k)) for word in range(2**k))
        values[size,k]=Dk
        discrepancies.append({'N':size,'k':k,'D_k':frac(Dk),'block_counts':dict(sorted(counts.items()))})
violations=[]
for size in [256,512,1024,2048]:
    for k in range(1,9):
        if values[2*size,k]>values[size,k]:
            violations.append({'N':size,'k':k,'D_N':frac(values[size,k]),'D_2N':frac(values[2*size,k])})
assert violations
emit(32, {'certified_binary_digits':N,'fractional_binary_hex':f'{digit_lo:01024x}',
          'certificate':'The lower and upper rational Machin bounds give the same floor of (pi-3)*2^4096. Arctangent series lengths: 1000 at 1/5 and 300 at 1/239.',
          'exact_discrepancies':discrepancies,'violations_of_monotone_doubling':violations,
          'limit':'Disproves only the proposed finite monotone-discrepancy shortcut; normal sequences can have such increases. No BBP recurrence or full normality theorem was proved.'})

print('All 27 bounded attempts completed.',flush=True)
