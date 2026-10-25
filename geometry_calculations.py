"""Reproducible bounded calculations for items 56--80. Standard library only.
Run: python tmp/math_work_round2/geometry_calculations.py
No global open conjecture is asserted to follow from these calculations.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
from itertools import product, combinations, permutations
from math import factorial, gcd, isqrt, comb
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent
results = {}

def det_mod(matrix, p):
    a = [[v % p for v in r] for r in matrix]
    assert len(a) == len(a[0])
    answer = 1
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None: return 0
        if k != j:
            a[j], a[k] = a[k], a[j]
            answer = -answer
        pivot = a[j][j]
        answer = answer * pivot % p
        inverse = pow(pivot, -1, p)
        for k in range(j+1, len(a)):
            q = a[k][j] * inverse % p
            for c in range(j, len(a)):
                a[k][c] = (a[k][c] - q * a[j][c]) % p
    return answer % p

def rank_certificate(matrix, prime=1009):
    a = [[v % prime for v in row] for row in matrix]
    row_ids = list(range(len(a)))
    selected_rows, selected_cols = [], []
    r = 0
    for c in range(len(a[0])):
        pivot = next((k for k in range(r, len(a)) if a[k][c]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        row_ids[r], row_ids[pivot] = row_ids[pivot], row_ids[r]
        selected_rows.append(row_ids[r]); selected_cols.append(c)
        inverse = pow(a[r][c], -1, prime)
        for k in range(r+1, len(a)):
            q = a[k][c] * inverse % prime
            for j in range(c, len(a[0])):
                a[k][j] = (a[k][j] - q * a[r][j]) % prime
        r += 1
        if r == len(a): break
    minor = [[matrix[i][j] for j in selected_cols] for i in selected_rows]
    determinant = det_mod(minor, prime) if r else 1
    assert determinant != 0
    return {"rows": len(matrix), "columns":len(matrix[0]), "rank_mod_prime":r,
            "prime":prime, "minor_rows_zero_based":selected_rows,
            "minor_columns_zero_based":selected_cols,"minor_determinant_mod_prime":determinant}

def matrix_inverse(a):
    n=len(a); b=[[F(v) for v in a[i]]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if b[k][j])
        b[j],b[k]=b[k],b[j]
        q=b[j][j]; b[j]=[v/q for v in b[j]]
        for i in range(n):
            if i!=j:
                q=b[i][j]; b[i]=[v-q*w for v,w in zip(b[i],b[j])]
    return [r[n:] for r in b]

def matmul(a,b):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]

# 56: exact Hessians of the standard sphere height function in pole charts.
results[56]={"height_charts":"h_plus/minus(x)=+/-sqrt(1-|x|^2)",
             "north_hessian":[[-int(i==j) for j in range(4)] for i in range(4)],
             "south_hessian":[[int(i==j) for j in range(4)] for i in range(4)],
             "morse_indices":[4,0],"critical_point_count":2}

# 57: numerator identity for inverse stereographic hemisphere parametrizations.
# 4r+(1-r)^2-(1+r)^2 is identically zero as a polynomial in r=|y|^2.
results[57]={"sphere_equation_numerator_coefficients":[1-1,4-2-2,1-1],
             "map":"(2y/(1+r), +/-(1-r)/(1+r)), r=|y|^2<=1",
             "inverse":"y=x/(1+/-t) on the matching hemisphere",
             "boundary":"r=1 gives t=0"}
assert results[57]["sphere_equation_numerator_coefficients"] == [0,0,0]

# 58: exact free-group words; relator multiplication, inversion, conjugation only.
def reduce_word(w):
    stack=[]
    for a in w:
        if stack and stack[-1]==-a: stack.pop()
        else: stack.append(a)
    return stack
def inv(w): return [-a for a in w[::-1]]
def apply_move(rs, op):
    rs=[r[:] for r in rs]
    if op[0]=='multiply':
        _,i,j,sign=op; rs[i]=reduce_word(rs[i]+(rs[j] if sign==1 else inv(rs[j])))
    elif op[0]=='invert': rs[op[1]]=inv(rs[op[1]])
    else:
        _,i,w=op; rs[i]=reduce_word(w+rs[i]+inv(w))
    return rs
def inverse_move(op):
    if op[0]=='multiply': return [op[0],op[1],op[2],-op[3]]
    if op[0]=='conjugate': return [op[0],op[1],inv(op[2])]
    return op
moves=[['multiply',0,1,1],['conjugate',1,[1]],['multiply',1,0,1],
       ['invert',0],['conjugate',0,[2,-1]],['multiply',0,1,1],
       ['conjugate',1,[-2,1]],['multiply',1,0,-1]]
rs=[[1],[2]]; forward=[rs]
for move in moves: rs=apply_move(rs,move); forward.append(rs)
start=rs; undo=[inverse_move(op) for op in moves[::-1]]; reverse=[rs]
for op in undo: rs=apply_move(rs,op); reverse.append(rs)
assert rs==[[1],[2]]
results[58]={"word_encoding":"1=x, -1=x^-1, 2=y, -2=y^-1",
             "presentation_relators":start,"reducing_moves":undo,"states":reverse,
             "origin":"Deliberately constructed from the trivial presentation, not an open candidate."}

# 59: radial Morse function restricted to the explicit standard disk.
results[59]={"disk":"(u,v,0,0), u^2+v^2<=1", "radial_squared":"u^2+v^2",
             "gradient":["2u","2v"],"hessian":[[2,0],[0,2]],
             "interior_critical_points":[[0,0]],"critical_indices":[0]}

# 60: trefoil Jones polynomial squared, exact integer convolution.
v={1:1,3:1,4:-1}; square={}
for i,x in v.items():
    for j,y in v.items(): square[i+j]=square.get(i+j,0)+x*y
square={i:x for i,x in square.items() if x}
results[60]={"trefoil_Jones_coefficients":v,"connected_sum_Jones_coefficients":square,
             "breadth":max(square)-min(square),"diagram_upper_bound":6,
             "deduction":"Jones breadth <= crossing number <= joined diagram crossings gives 6."}
assert results[60]['breadth']==6

# 61: necessary first-homology filter on a completely stated finite slope set.
slopes=[(p,q) for p in range(-4,5) for q in range(1,5) if gcd(p,q)==1]
pairs=list(combinations(slopes,2))
excluded=[(a,b) for a,b in pairs if abs(a[0])!=abs(b[0])]
results[61]={"slopes":slopes,"unordered_pairs":len(pairs),
             "excluded_by_H1_order_or_rank":len(excluded),
             "surviving_pairs":len(pairs)-len(excluded),
             "formula":"H_1(S^3_{p/q}(K);Z)=Z/pZ, with p=0 interpreted as Z"}

# 62: arbitrary precision Decimal evaluation, independently repeated precision.
def atan_inverse(n, precision):
    x=D(1)/n; term=x; total=term; k=1
    threshold=D(10)**(-precision-8)
    while abs(term)>threshold:
        term*=-(x*x); total+=term/(2*k+1); k+=1
    return total
def decimal_pi(precision): return 16*atan_inverse(5,precision)-4*atan_inverse(239,precision)
def decimal_sin(x, precision):
    term=total=x; k=1; threshold=D(10)**(-precision-8)
    while abs(term)>threshold:
        term*=-(x*x)/((2*k)*(2*k+1)); total+=term; k+=1
    return total
def figure_eight(n, precision):
    with localcontext() as ctx:
        ctx.prec=precision+15; pi=decimal_pi(precision)
        term=total=D(1)
        for j in range(1,n):
            term*=4*decimal_sin(pi*j/n,precision)**2; total+=term
        value=2*pi/n*total.ln()
        ctx.prec=precision
        return str(+value),str(+total)
vals=[]
for n in [20,40,80]:
    low,jlo=figure_eight(n,70); high,jhi=figure_eight(n,130)
    difference=abs(D(low)-D(high))
    assert difference<D('1e-65')
    vals.append({"N":n,"scaled_log_at_70_digits":low,"scaled_log_at_130_digits":high,
                 "absolute_precision_difference":str(difference),"J_N_at_130_digits":jhi})
results[62]={"root_of_unity_formula":"J_N(4_1;exp(2*pi*i/N))=sum_{k=0}^{N-1} product_{j=1}^k 4 sin^2(pi*j/N)",
             "evaluations":vals,"arithmetic_status":"Two-precision numerical agreement, not an interval enclosure or a convergence proof."}

# 63: the exact arithmetic gap between two inequalities, not a realizability claim.
gaps=[{"k":k,"Furuta_min_l":2*k+1,"eleven_eighths_min_l":3*k,
       "integer_l_between":[l for l in range(2*k+1,3*k)]} for k in range(1,9)]
results[63]={"form":"2k(-E8) direct_sum lH","b2":"16k+2l","signature":"-16k",
             "table":gaps,"total_gap_pairs":sum(len(a['integer_l_between']) for a in gaps),
             "warning":"This compares the older 10/8+2 bound only; stronger known restrictions are not applied."}

# 64: explicit induced integral automorphism in a five-torus calibration.
a=[[1,2,0,0,1],[0,1,3,0,0],[0,0,1,4,0],[0,0,0,1,5],[0,0,0,0,1]]
ainv=matrix_inverse(a); identity=matmul(a,ainv)
assert identity==[[int(i==j) for j in range(5)] for i in range(5)]
assert all(v.denominator==1 for r in ainv for v in r)
results[64]={"A":a,"A_inverse":[[int(v) for v in r] for r in ainv],
             "equivariant_homotopy":"H_s(x)=(1-s)F(x)+sAx; H_s(x+z)=H_s(x)+Az"}

# 65 and 66: exact restricted proofs are in geometry_restricted_proofs.md.
results[65]={"dimension":2,"L_class":"1", "higher_signature":"<f^*a,[M]> for a in H^2(Bpi;Q)",
             "identity":"<(f o h)^*a,[N]>=<f^*a,h_*[N]>=<f^*a,[M]>"}
def dihedral_mul(a,b): return (a[0]+((-1)**a[1])*b[0],(a[1]+b[1])%2)
t=(1,0); r=(0,1)
assert dihedral_mul(dihedral_mul(r,t),r)==(-1,0)
results[66]={"group":"Z semidirect C2 with inversion", "r_t_r":list(dihedral_mul(dihedral_mul(r,t),r)),
             "cyclic_subgroup_index":2,"classifying_space":"E_VCyc(G)=point", "assembly_map":"identity"}

# 67: cubic discriminant and Eisenstein coefficient checks.
coeffs=[1,0,0,-2]
disc=-27*(-2)**2
assert all(c%2==0 for c in coeffs[1:]) and coeffs[-1]%4!=0
results[67]={"polynomial":"x^3-2","Eisenstein_prime":2,"discriminant":disc,
             "discriminant_is_rational_square":False,"Galois_group":"S3"}

# 68: count all normalized projective points of the split quadric over F_7.
q=7; projective=[]
for first in range(4):
    for tail in product(range(q),repeat=3-first):
        projective.append((0,)*first+(1,)+tail)
quadric=[v for v in projective if (v[0]*v[1]-v[2]*v[3])%q==0]
assert len(quadric)==(q+1)**2
results[68]={"field":"F7","equation":"x0*x1-x2*x3=0", "projective_points_checked":len(projective),
             "quadric_point_count":len(quadric),"formula":"#Q(F_{7^r})=(7^r+1)^2",
             "ruling_intersection_matrix":[[0,1],[1,0]],"intersection_determinant":-1,
             "cycle_field_and_coefficients":"Both rulings defined over F7; use Q_l coefficients, l != 7."}

# 69: compute the exterior product Lefschetz map, with algebraic inverse described in proof.
def wedge_monomials(a,b):
    if set(a)&set(b): return 0,()
    inversions=sum(x>y for x in a for y in b)
    return (-1)**inversions,tuple(sorted(a+b))
h=[(0,1),(2,3)]; h3basis=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
lef=[[0]*4 for _ in range(4)]
for col in range(4):
    for mon in h:
        sign,term=wedge_monomials(mon,(col,))
        if sign: lef[h3basis.index(term)][col]+=sign
assert matmul(lef,lef)==[[int(i==j) for j in range(4)] for i in range(4)]
h_squared=sum(wedge_monomials(x,y)[0] for x in h for y in h)
assert h_squared==2
results[69]={"variety":"E x E, E: y^2=x^3-x", "H1_basis":["a1","b1","a2","b2"],
             "H3_basis":["a1b1a2","a1b1b2","a1a2b2","b1a2b2"],
             "L_H1_to_H3_matrix":lef,"L_inverse_same_matrix":True,"h_squared_top_coefficient":2,
             "algebraic_inverse":"C1+C2 on H3, where Ci integrates factor i and is the product of E x E with the other diagonal."}

# 70: exact section count on C x C x E x E.
results[70]={"variety":"C x C x E x E; C: y^2=x^5-1 (smooth completion), E: y^2=x^3-x",
             "genera":[2,2,1,1],"dimension":4,"canonical_section_counts":[{"m":m,"h0":1 if m==0 else (4 if m==1 else (2*m-1)**2)} for m in range(7)],
             "formula_m_ge_2":"h0(mK_X)=(2m-1)^2", "numerical_dimension":2,
             "K_X":"pullback of K_(C x C), hence globally generated and nef"}

# 71: exact nonterminating scalar descent; not a geometric sequence of flips.
sequence=[F(1)]
for _ in range(10): sequence.append(sequence[-1]/(1+sequence[-1]))
assert sequence==[F(1,n) for n in range(1,12)]
assert all(a>b>0 for a,b in zip(sequence,sequence[1:]))
results[71]={"recurrence":"x_(n+1)=x_n/(1+x_n), x_0=1", "closed_form":"x_n=1/(n+1)",
             "first_eleven":[str(v) for v in sequence],"gap":"Strict descent in nonnegative real values does not imply well-founded descent."}

# 72--73: actual characteristic-zero interpolation, certified using nonzero integer minors modulo 1009.
points=[(i,(i*i+i**5)%101) for i in range(10)]
def falling(n,k): return factorial(n)//factorial(n-k)
def interpolation(d,mults):
    cols=[(a,total-a) for total in range(d+1) for a in range(total+1)]
    rows=[]; labels=[]
    for index,((x,y),m) in enumerate(zip(points,mults)):
        for total in range(m):
            for u in range(total+1):
                v=total-u
                rows.append([0 if a<u or b<v else falling(a,u)*falling(b,v)*x**(a-u)*y**(b-v) for a,b in cols])
                labels.append([index,u,v])
    return rows,cols,labels
interpolation_output={"integer_points":points,"row_meaning":"[point_index, dx_order, dy_order]", "tests":[]}
nagata=[]
for m in [1,2,3]:
    d=isqrt(10*m*m); matrix,cols,rows=interpolation(d,[m]*10)
    cert=rank_certificate(matrix)
    assert cert['rank_mod_prime']==len(cols)
    test={"id":72,"m":m,"d":d,"multiplicities":[m]*10,"column_monomials":cols,"row_labels":rows,**cert}
    interpolation_output['tests'].append(test); nagata.append({k:v for k,v in test.items() if k not in ['column_monomials','row_labels']})
results[72]={"points":points,"tests":nagata,"deduction":"Full column rank over F1009 supplies a nonzero integer minor, hence no nonzero Q/C polynomial at this configuration; openness gives the same for very general points."}
shgh=[]
for d,mults in [(4,[2]+[1]*9),(4,[2,2]+[1]*8),(5,[2]*5+[1]*5),(2,[2,2]+[0]*8)]:
    matrix,cols,rows=interpolation(d,mults); cert=rank_certificate(matrix)
    test={"id":73,"d":d,"multiplicities":mults,"column_monomials":cols,"row_labels":rows,**cert}
    test['kernel_dimension_over_modular_field']=len(cols)-cert['rank_mod_prime']
    if d==2:
        coeff={(2,0):4,(1,1):-4,(0,2):1}
        witness=[coeff.get(tuple(c),0) for c in cols]
        assert all(sum(a*b for a,b in zip(row,witness))==0 for row in matrix)
        assert cert['rank_mod_prime']==5
        test['exact_kernel_witness']=witness; test['witness_polynomial']='(y-2x)^2'
    else: assert cert['rank_mod_prime']==len(matrix)
    interpolation_output['tests'].append(test); shgh.append({k:v for k,v in test.items() if k not in ['column_monomials','row_labels']})
results[73]={"tests":shgh,"special_case_geometry":"D=2(H-E1-E2)=2E, E^2=-1, D.E=-2"}
(OUT/'geometry_interpolation_certificates.json').write_text(json.dumps(interpolation_output,indent=2),encoding='utf-8')

# 74: 6D Pfaffian count and exact cancellation against sphere volume.
def pairings(items):
    if not items: return [()]
    first,*rest=items; out=[]
    for j,other in enumerate(rest):
        for tail in pairings(rest[:j]+rest[j+1:]): out.append(((first,other),)+tail)
    return out
ps=pairings(list(range(6)))
assert len(ps)==15
results[74]={"dimension":6,"Pfaffian_pairings":len(ps),"Euler_density":"15*kappa^3/(8*pi^3) dvol",
             "unit_sphere_volume":"16*pi^3/15","Euler_integral_unit_sphere":str(F(15,8)*F(16,15))}

# 75: symbolic minimum-point obstruction, with proof in companion markdown.
results[75]={"metric_class":"exp(2f) times the standard product metric on S2 x S2, f any smooth real function",
             "point":"global minimum of f", "mixed_plane_curvature":"exp(-2f)(-Hess f(X,X)-Hess f(Y,Y)) <= 0",
             "conditions_used":["compactness supplies a minimum","df=0 there","Hess f positive semidefinite","product mixed sectional curvature zero"]}

# 76: formal first-derivative tensor; all arithmetic factored through sqrt(5).
lambdas=[-3,-1,1,3]; tensor={}
for indices,coefficient in [((0,0,0),2),((0,1,1),-4),((0,2,2),2)]:
    for perm in set(permutations(indices)): tensor[perm]=coefficient
trace=[sum(tensor.get((i,i,k),0) for i in range(4)) for k in range(4)]
weighted=[sum(lambdas[i]*tensor.get((i,i,k),0) for i in range(4)) for k in range(4)]
cofactors=[-3,-9,9,3]
dk=[sum(cofactors[i]*tensor.get((i,i,k),0) for i in range(4)) for k in range(4)]
norm=5*sum(v*v for v in tensor.values()); s=sum(v*v for v in lambdas)
assert trace==weighted==[0]*4 and dk==[48,0,0,0] and norm==s*(s-4)==320
results[76]={"principal_curvatures":lambdas,"S":s,"K":9,
             "nonzero_T_entries_in_units_sqrt5":[[list(k),v] for k,v in sorted(tensor.items())],
             "derivative_trace_in_units_sqrt5":trace,"lambda_weighted_trace_in_units_sqrt5":weighted,
             "gradient_K_in_units_sqrt5":dk,"norm_T_squared":norm,"Simons_required_S_times_S_minus_n":s*(s-4),
             "scope":"Necessary pointwise and first-derivative constraints only; no assertion of prolongation, local immersion, or compact realization."}

# 77: exact volume formulas for an entire family of centrally symmetric polytopes.
def family_volumes(t):
    primal=t+F(1,4)
    q=1/(2*t)
    cdf=((2-q)**4-4*(1-q)**4)/24
    polar=16*(1-2*cdf)
    alternative=F(32,3)/t-F(4,3)/t**3+F(1,4)/t**4
    assert polar==alternative
    gap=primal*polar-F(32,3)
    u=2*t-1
    assert gap==(16*u**3+32*u**2+14*u+1)/(48*t**4)
    return {"t":str(t),"primal_volume":str(primal),"polar_volume":str(polar),"volume_product":str(primal*polar),"gap_above_32_over_3":str(gap)}
results[77]={"family":"conv(+/-e_i, +/-t(1,1,1,1)), t>=1/2", "primal_volume":"t+1/4",
             "polar_volume":"32/(3t)-4/(3t^3)+1/(4t^4)",
             "gap_formula":"(16u^3+32u^2+14u+1)/(48t^4), u=2t-1>=0", 
             "samples":[family_volumes(t) for t in [F(1,2),F(3,4),F(1),F(3,2),F(2)]]}

# 78: two explicit locally nilpotent derivations preserve the hypersurface relation.
results[78]={"ring":"C[x,y,z]/(xy-z^2+1)","delta":{"x":"0","y":"2z","z":"x"},
             "epsilon":{"x":"2z","y":"0","z":"y"},
             "delta_relation":"x(2z)-2z*x=0","epsilon_relation":"(2z)y-2z*y=0",
             "delta_chains":{"x":["x","0"],"y":["y","2z","2x","0"],"z":["z","x","0"]},
             "epsilon_chains":{"y":["y","0"],"x":["x","2z","2y","0"],"z":["z","y","0"]},
             "failed_invariance":"delta(x)=0 but epsilon(x)=2z != 0"}

# 79: a fixed surface with a verified negative irreducible curve.
conic_points=[(i,i*i,1) for i in range(10)]
assert all(y*z-x*x==0 for x,y,z in conic_points)
assert len(set(conic_points))==10
c_squared=2*2-10; canonical_dot=-3*2+10
results[79]={"points_on_conic_yz_x2":conic_points,"blowup_count":10,
             "strict_transform_class":"2H-sum(E_i)","self_intersection":c_squared,"canonical_intersection":canonical_dot,
             "adjunction_2g_minus_2":c_squared+canonical_dot,"genus":1+(c_squared+canonical_dot)//2,
             "conic_smoothness":"gradient=(-2x,z,y) cannot vanish at a projective point"}

# 80: D4 exact determinant, shortest-vector witness, one explicit periodic perturbation obstruction.
basis=[[1,-1,0,0],[0,1,-1,0],[0,0,1,-1],[0,0,1,1]]
roots=[v for v in product(range(-1,2),repeat=4) if sum(v)%2==0 and sum(x*x for x in v)==2]
assert len(roots)==24 and det_mod(basis,1009)==2
perturbations=[]
for step in [F(1,10),F(1,4),F(1,2),F(1),F(3,2)]:
    upper=2-2*step+step*step
    assert upper<2
    perturbations.append({"s":str(step),"min_squared_distance_upper_bound":str(upper),"density_ratio_upper_bound":str((upper/F(2))**2)})
results[80]={"D4_basis_rows":basis,"covolume":2,"shortest_squared_norm":2,"shortest_vectors":roots,
             "density":"pi^2/16", "two_coset_cell":"L=<2b1,b2,b3,b4>; D4=L union (b1+L)",
             "perturbation":"Replace b1+L by b1+s*e1+L, keep L fixed",
             "distance_upper_bound":"min(2+2s+s^2,2-2s+s^2)=2-2|s|+s^2<2 for 0<|s|<2",
             "samples":perturbations}

assert sorted(results)==list(range(56,81))
(OUT/'geometry_calculations.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({"items":len(results),"nagata":[[a['m'],a['rows'],a['columns'],a['rank_mod_prime'],a['minor_determinant_mod_prime']] for a in nagata],
                  "shgh":[[a['d'],a['multiplicities'],a['rank_mod_prime'],a['kernel_dimension_over_modular_field']] for a in shgh],
                  "cosmetic_pairs_excluded":len(excluded),"volume_scaled_logs":[[a['N'],a['scaled_log_at_70_digits'][:24]] for a in vals],
                  "output":str(OUT/'geometry_calculations.json')},indent=2))
