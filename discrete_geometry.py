import itertools as it, collections as co, random, json, pathlib
from fractions import Fraction as F
OUT=pathlib.Path(__file__).parent

# 42: exact arithmetic in Q(sqrt(3),sqrt(11)), basis 1,sqrt3,sqrt11,sqrt33.
def q(a=0,b=0,c=0,d=0):return tuple(map(F,(a,b,c,d)))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,b):
    c=[F(0)]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i^j]+=x*y*(3 if i&j&1 else 1)*(11 if i&j&2 else 1)
    return tuple(c)
P=[(q(),q()),(q(b=1),q()),(q(b=F(1,2)),q(F(1,2))),(q(b=F(1,2)),q(F(-1,2))),
   (q(b=F(5,6)),q(d=F(1,6))),(q(b=F(5,12),c=F(-1,12)),q(F(5,12),d=F(1,12))),(q(b=F(5,12),c=F(1,12)),q(F(-5,12),d=F(1,12)))]
E=[];distance_checks=[]
for a,b in it.combinations(range(7),2):
    dx=sub(P[a][0],P[b][0]);dy=sub(P[a][1],P[b][1]);d=add(mul(dx,dx),mul(dy,dy))
    if d==q(1):E.append((a,b))
    distance_checks.append({'pair':[a,b],'squared_distance_coefficients':[str(x) for x in d]})
def color(k):
    A=[set() for _ in range(7)]
    for a,b in E:A[a].add(b);A[b].add(a)
    order=sorted(range(7),key=lambda i:(-len(A[i]),i));colors=[-1]*7;leaves=0
    def go(t):
        nonlocal leaves
        if t==7:leaves+=1;return list(colors)
        v=order[t]
        for c in range(k):
            if all(colors[w]!=c for w in A[v]):
                colors[v]=c;r=go(t+1)
                if r is not None:return r
                colors[v]=-1
        return None
    return go(0)
assert len(E)==11 and color(3) is None
r42={'vertices':7,'edges':E,'exact_coordinates':[[[str(c) for c in x],[str(c) for c in y]] for x,y in P],'coordinate_basis':['1','sqrt(3)','sqrt(11)','sqrt(33)'],'all_21_squared_distances':distance_checks,'three_coloring':None,'four_coloring':color(4),'chromatic_number':4,'proof':'Each diamond consists of two triangles sharing an edge. In a three-coloring its two degree-two endpoints have the same color. The two diamonds share endpoint 0, forcing vertices 1 and 4 to share its color, but edge 1-4 is present.'}

# 43: independent toy grid; these are not instances of the 2026 tower construction.
grid=list(it.product(range(9),repeat=2))
def d2(a,b):return (a[0]-b[0])**2+(a[1]-b[1])**2
def stats(P):
    C=co.Counter(d2(a,b) for a,b in it.combinations(P,2));R=max(C.values())
    return {'points':len(P),'U_fixed_squared_distance_1':C[1],'R_maximum_multiplicity':R,'maximizing_squared_distances':sorted(d for d,c in C.items() if c==R)}
def prune(mode):
    P=list(grid);C=co.Counter(d2(a,b) for a,b in it.combinations(P,2));trace=[]
    while len(P)>50:
        best=None;remove=None;delta=None
        for a in P:
            dec=co.Counter(d2(a,b) for b in P if b!=a)
            score=C[1]-dec[1] if mode=='U' else max(c-dec[d] for d,c in C.items())
            if best is None or score>best:best=score;remove=a;delta=dec
        P.remove(remove);C.subtract(delta);trace.append({'removed':remove,'remaining_objective':best})
    return {'retained_points':P,'statistics':stats(P),'deletion_trace':trace}
rng=random.Random(43);randomstats=[stats(rng.sample(grid,50)) for _ in range(100)]
r43={'grid_statistics':stats(grid),'R_pruning':prune('R'),'U_pruning':prune('U'),'random_subsets':100,'random_R_range':[min(x['R_maximum_multiplicity'] for x in randomstats),max(x['R_maximum_multiplicity'] for x in randomstats)],'random_U_range':[min(x['U_fixed_squared_distance_1'] for x in randomstats),max(x['U_fixed_squared_distance_1'] for x in randomstats)],'number_field_construction_status':'No suitable <=200-point input established; feasibility remains unresolved.'}

# 44: exact finite-direction covers for three explicit rational polytopes.
signs=list(it.product((-1,1),repeat=3));axes=[tuple(s if j==i else 0 for j in range(3)) for i in range(3) for s in (-1,1)]
polytopes=[('cube',signs,[(a,1) for a in axes]),('octahedron',axes,[(a,1) for a in signs]),('cuboctahedron',sorted({p for p in it.product((-1,0,1),repeat=3) if sum(abs(v) for v in p)==2}),[(a,1) for a in axes]+[(a,2) for a in signs])]
directions=[d for d in it.product((-1,0,1),repeat=3) if any(d)];dot=lambda a,b:sum(x*y for x,y in zip(a,b));illum=[]
for name,vertices,facets in polytopes:
    assert all(dot(a,v)<=b for v in vertices for a,b in facets)
    incident=[[a for a,b in facets if dot(a,v)==b] for v in vertices]
    covers={}
    for d in directions:
        mask=sum(1<<i for i,ns in enumerate(incident) if all(dot(a,d)<0 for a in ns))
        if mask and mask not in covers:covers[mask]=d
    # Remove dominated coverage masks; this preserves optimal cover cardinality.
    useful=[m for m in covers if not any(m!=t and m&t==m for t in covers)]
    full=(1<<len(vertices))-1;winner=None;checks=0
    for k in range(1,9):
        for choice in it.combinations(useful,k):
            checks+=1;union=0
            for c in choice:union|=c
            if union==full:winner=choice;break
        if winner:break
    assert winner
    illum.append({'polytope':name,'vertices':vertices,'facet_inequalities':facets,'dictionary_directions':26,'distinct_nondominated_cover_masks':len(useful),'minimum_cover_in_dictionary':len(winner),'cover_directions':[covers[m] for m in winner],'covered_vertex_indices':[[i for i in range(len(vertices)) if m>>i&1] for m in winner],'combinations_checked':checks})
r44={'polytopes':illum}

# 47: exact orientation controls, including a sought eight-point lower-bound example.
def orient(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def general(P):return all(orient(a,b,c)!=0 for a,b,c in it.combinations(P,3))
def hull(P):
    P=sorted(P);lo=[];hi=[]
    for p in P:
        while len(lo)>=2 and orient(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in P[::-1]:
        while len(hi)>=2 and orient(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
grid4=list(it.product(range(4),repeat=2));gp=0;bad=[]
for P in it.combinations(grid4,5):
    if not general(P):continue
    gp+=1
    if not any(len(hull(S))==4 for S in it.combinations(P,4)):bad.append(P)
negative=[(0,0),(3,0),(0,3),(1,1)];assert general(negative) and len(hull(negative))==3
rng=random.Random(47);grid21=list(it.product(range(21),repeat=2));eight=None;general8=0
for trial in range(1,10001):
    P=rng.sample(grid21,8)
    if not general(P):continue
    general8+=1
    if not any(len(hull(S))==5 for S in it.combinations(P,5)):eight=sorted(P);break
r47={'five_subsets_considered':4368,'five_point_general_position_subsets':gp,'five_point_sets_without_convex_quadrilateral':bad,'four_point_negative_control':negative,'eight_point_search_proposals':trial,'eight_point_general_position_proposals':general8,'eight_point_set_without_convex_pentagon':eight,'five_subsets_verified_in_eight_point_witness':56 if eight else 0}

# 48: every cycle on each fixed convex point set, up to reversal and cyclic shift.
cycledata=[]
for n in range(3,10):
    good=[];tested=0
    for rest in it.permutations(range(1,n)):
        if rest[0]>rest[-1]:continue
        p=(0,)+rest;tested+=1;edges=[tuple(sorted((p[i],p[(i+1)%n]))) for i in range(n)];ok=True
        for (a,b),(c,d) in it.combinations(edges,2):
            if len({a,b,c,d})<4:continue
            if (a<c<b)==(a<d<b):ok=False;break
        if ok:good.append(p)
    cycledata.append({'n':n,'cycles_tested':tested,'straight_convex_thrackle_cycles':len(good),'witnesses':good})
r48={'convex_point_coordinates':'(i,i^2), for i=0,...,n-1','orders':cycledata}
res={'42':r42,'43':r43,'44':r44,'47':r47,'48':r48};(OUT/'discrete_geometry_results.json').write_text(json.dumps(res,indent=2)+'\n')
print('42 edges/chromatic',len(E),r42['chromatic_number'])
print('43',r43['grid_statistics'],r43['R_pruning']['statistics'],r43['U_pruning']['statistics'],r43['random_R_range'])
print('44',[(x['polytope'],x['minimum_cover_in_dictionary']) for x in illum])
print('47',r47)
print('48',[(x['n'],x['cycles_tested'],x['straight_convex_thrackle_cycles']) for x in cycledata])
