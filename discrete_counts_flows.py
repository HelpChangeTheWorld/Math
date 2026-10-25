import itertools as it, collections as co, random, json, pathlib, functools, math
from fractions import Fraction as F
OUT=pathlib.Path(__file__).parent

def interval_intersect(A,B):
    i=j=0;out=[]
    while i<len(A) and j<len(B):
        lo=max(A[i][0],B[j][0]);hi=min(A[i][1],B[j][1])
        if lo<=hi:
            if out and lo<=out[-1][1]:out[-1]=(out[-1][0],max(hi,out[-1][1]))
            else:out.append((lo,hi))
        if A[i][1]<B[j][1]:i+=1
        else:j+=1
    return out
def permitted(speeds,d):
    A=[(F(0),F(1))]
    for v in speeds:
        A=interval_intersect(A,[((m+d)/v,(m+1-d)/v) for m in range(v)])
        if not A:break
    return A
deltas=[F(1,15),F(1,15)+F(1,1500),F(1,14)];rng=random.Random(45);speedsets=[];proposals=0
while len(speedsets)<500 and proposals<2000:
    proposals+=1;s=sorted(rng.sample(range(1,101),14))
    if math.gcd(*s)==1:speedsets.append(s)
run=[]
for s in speedsets:
    tests=[]
    for d in deltas:
        A=permitted(s,d);t=A[0][0] if A else None
        if t is not None:assert all(min((t*v)%1,1-(t*v)%1)>=d for v in s)
        tests.append({'threshold':str(d),'components':len(A),'witness':str(t) if t is not None else None,'total_length':str(sum((b-a for a,b in A),F(0)))})
    rel3=sum(a+b==c for a,b in it.combinations(s,2) for c in s if c not in (a,b))
    sums=co.defaultdict(list)
    for a,b in it.combinations(s,2):sums[a+b].append({a,b})
    rel4=sum(not (a&b) for groups in sums.values() for a,b in it.combinations(groups,2))
    run.append({'speeds':s,'three_term_relations':rel3,'four_term_relations':rel4,'tests':tests})
baseline=permitted(list(range(1,15)),F(1,15));assert baseline and not permitted(list(range(1,15)),F(1,15)+F(1,1500))
r45={'proposals':proposals,'retained_gcd_one_sets':len(run),'thresholds':[str(d) for d in deltas],'feasible_counts':[sum(x['tests'][i]['components']>0 for x in run) for i in range(3)],'baseline_speeds':list(range(1,15)),'baseline_feasible_intervals':[[str(a),str(b)] for a,b in baseline],'sample':run}

# 46: exact counts for genuinely new 8-10 vertex orders.
def count_extensions(pred):
    n=len(pred)
    @functools.lru_cache(None)
    def dp(mask):
        if mask==(1<<n)-1:return 1
        return sum(dp(mask|1<<v) for v in range(n) if not (mask>>v&1) and pred[v]&mask==pred[v])
    return dp(0)
rng=random.Random(46);posets=[];signatures={};collision=None;within_collision=None;paircount=0
for case in range(100):
    n=8+case%3;succ=[0]*n
    for i,j in it.combinations(range(n),2):
        if rng.random()<F(1,3):succ[i]|=1<<j
    for k in range(n-1,-1,-1):
        for i in range(k):
            if succ[i]>>k&1:succ[i]|=succ[k]
    perm=list(range(n));rng.shuffle(perm);rels=[(perm[i],perm[j]) for i in range(n) for j in range(n) if succ[i]>>j&1]
    pred=[0]*n;succ=[0]*n
    for i,j in rels:pred[j]|=1<<i;succ[i]|=1<<j
    inc=[((1<<n)-1) ^ (pred[i]|succ[i]|1<<i) for i in range(n)]
    if not any(inc):continue
    den=count_extensions(tuple(pred));rows=[];local={}
    for x in range(n):
        for y in range(n):
            if not (inc[x]>>y&1):continue
            paircount+=1;p=list(pred);p[y]|=1<<x;num=count_extensions(tuple(p));balanced=den<=3*num<=2*den
            sig=(inc[x].bit_count(),inc[y].bit_count(),(inc[x]&inc[y]).bit_count(),pred[x].bit_count(),pred[y].bit_count(),succ[x].bit_count(),succ[y].bit_count())
            row={'case':case,'n':n,'pair':[x,y],'signature':sig,'numerator':num,'denominator':den,'probability':str(F(num,den)),'balanced':balanced,'strict_order_relations':rels}
            if sig in signatures and signatures[sig]['balanced']!=balanced and collision is None:collision=[signatures[sig],row]
            if sig in local and local[sig]['balanced']!=balanced and within_collision is None:within_collision=[local[sig],row]
            signatures.setdefault(sig,row);local.setdefault(sig,row);rows.append({'pair':[x,y],'probability':str(F(num,den)),'balanced':balanced})
    posets.append({'case':case,'n':n,'strict_order_relations':rels,'extensions':den,'pairs':rows})
r46={'posets':len(posets),'ordered_incomparable_pairs':paircount,'signature_count':len(signatures),'balanced_unbalanced_signature_collision':collision,'within_poset_collision':within_collision,'all_posets_have_balanced_pairs':all(any(p['balanced'] for p in x['pairs']) for x in posets),'cases':posets}

# 51: exact covers in a prescribed one-edge perturbation neighborhood.
def emask(t):return sum(1<<(7*i+v) for i,v in enumerate(t))
seed=[tuple(3*c+t for t in (x,y,(x+y)%3,(x+2*y)%3)) for c in (0,1) for x,y in it.product(range(3),repeat=2)]
def matching_two(edges):
    return any(not(a&b) for a,b in it.combinations(edges,2)) and not any(not(a&b or a&c or b&c) for a,b,c in it.combinations(edges,3))
def cover(edges,k):
    @functools.lru_cache(None)
    def solve(es,k):
        if not es:return ()
        if not k:return None
        freq=co.Counter(v for e in es for v in range(28) if e>>v&1)
        if len(es)>k*max(freq.values()):return None
        e=min(es,key=lambda e:sum(freq[v] for v in range(28) if e>>v&1))
        for v in sorted((v for v in range(28) if e>>v&1),key=lambda v:(-freq[v],v)):
            r=solve(tuple(t for t in es if not(t>>v&1)),k-1)
            if r is not None:return (v,)+r
        return None
    return solve(tuple(sorted(edges)),k)
base=list(map(emask,seed));assert matching_two(base) and cover(base,5) is None and cover(base,6) is not None
rng=random.Random(51);perturb=[];rejected=0
for case in range(100):
    deleted=rng.choice(seed)
    while True:
        added=tuple(rng.randrange(7) for _ in range(4))
        if added not in seed:break
    tuples=[e for e in seed if e!=deleted]+[added];edges=list(map(emask,tuples))
    if not matching_two(edges):rejected+=1;continue
    answer=None;tau=None
    for k in range(1,8):
        answer=cover(edges,k)
        if answer is not None:tau=k;break
    assert answer is not None and all(any(e>>v&1 for v in answer) for e in edges)
    perturb.append({'case':case,'deleted_edge':deleted,'added_edge':added,'matching_number':2,'cover_number':tau,'cover_vertices':[[v//7,v%7] for v in answer]})
r51={'seed_edges':seed,'seed_matching_number':2,'seed_cover_number':6,'proposals':100,'rejected_matching_constraint':rejected,'retained':len(perturb),'cover_number_distribution':dict(co.Counter(x['cover_number'] for x in perturb)),'cases':perturb}

# 55: exact augmenting-path network flow, independent of floating-point solvers.
def maxflow(N,arcs,s,t):
    R=[{} for _ in range(N)];orig={}
    for u,v,c in arcs:
        R[u][v]=R[u].get(v,0)+c;R[v].setdefault(u,0);orig[(u,v)]=orig.get((u,v),0)+c
    total=0
    while True:
        prev={s:None};Q=[s]
        for u in Q:
            for v,c in R[u].items():
                if c>0 and v not in prev:prev[v]=u;Q.append(v)
            if t in prev:break
        if t not in prev:break
        v=t;amount=10**9
        while v!=s:u=prev[v];amount=min(amount,R[u][v]);v=u
        v=t
        while v!=s:u=prev[v];R[u][v]-=amount;R[v][u]+=amount;v=u
        total+=amount
    return total,{e:c-R[e[0]][e[1]] for e,c in orig.items()}
def orient_degrees(n,E,H):
    m=len(E);s=m+n;t=s+1;arcs=[]
    for e,(u,v) in enumerate(E):arcs.extend([(s,e,1),(e,m+u,1),(e,m+v,1)])
    arcs.extend((m+v,t,4 if v in H else 1) for v in range(n))
    value,Flo=maxflow(t+1,arcs,s,t)
    if value!=m:return None
    oriented=[(u,v) if Flo[(e,m+u)]==1 else (v,u) for e,(u,v) in enumerate(E)]
    assert all(sum(a==v for a,b in oriented)==(4 if v in H else 1) for v in range(n))
    return oriented
def lift(n,O):
    div=[0]*n
    for u,v in O:div[u]+=1;div[v]-=1
    assert all(x%3==0 for x in div);b=[x//3 for x in div];s=n;t=n+1;arcs=[(u,v,1) for u,v in O]
    arcs.extend((s,v,x) for v,x in enumerate(b) if x>0);arcs.extend((v,t,-x) for v,x in enumerate(b) if x<0)
    val,Flo=maxflow(n+2,arcs,s,t);assert val==sum(x for x in b if x>0)
    f=[1-3*Flo[e] for e in O];check=[0]*n
    for (u,v),x in zip(O,f):check[u]+=x;check[v]-=x
    assert not any(check) and all(x in (1,-2) for x in f)
    return f
out=[]
for n in [6,8,10,12]:
    E=sorted({tuple(sorted((i,(i+d)%n))) for i in range(n) for d in [1,-1,2,-2,n//2]})
    lam=min(sum(bool(mask>>u&1)!=bool(mask>>v&1) for u,v in E) for mask in range(1,1<<n) if mask&1 and mask!=(1<<n)-1)
    counts=0;feasible=0;witness=None
    for H in it.combinations(range(n),n//2):
        counts+=1;O=orient_degrees(n,E,set(H))
        if O is None:continue
        feasible+=1;f=lift(n,O)
        if witness is None:witness={'high_outdegree_vertices':H,'oriented_edges':O,'signed_flow_values':f}
    out.append({'n':n,'edges':E,'exact_edge_connectivity':lam,'balanced_type_assignments_tested':counts,'feasible_assignments':feasible,'verified_integer_lifts':feasible,'witness':witness})
r55={'circulants':out,'total_assignments':sum(x['balanced_type_assignments_tested'] for x in out),'total_verified_lifts':sum(x['verified_integer_lifts'] for x in out)}
res={'45':r45,'46':r46,'51':r51,'55':r55};(OUT/'discrete_count_flow_results.json').write_text(json.dumps(res,indent=2)+'\n')
print('45',r45['retained_gcd_one_sets'],r45['feasible_counts'],'baseline',r45['baseline_feasible_intervals'])
print('46',{k:v for k,v in r46.items() if k not in ['cases','balanced_unbalanced_signature_collision','within_poset_collision']},'collision',None if collision is None else [(x['case'],x['pair'],x['probability'],x['balanced']) for x in collision],'within',None if within_collision is None else [(x['case'],x['pair'],x['probability'],x['balanced']) for x in within_collision])
print('51',{k:v for k,v in r51.items() if k not in ['cases','seed_edges']})
print('55',[(x['n'],x['exact_edge_connectivity'],x['balanced_type_assignments_tested'],x['feasible_assignments']) for x in out])
