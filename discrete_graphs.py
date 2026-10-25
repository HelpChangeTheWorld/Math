import itertools as it, collections as co, random, json, pathlib, math
OUT=pathlib.Path(__file__).parent
def edge(a,b): return (min(a,b),max(a,b))
def adj(n,E):
    A=[set() for _ in range(n)]
    for a,b in E: A[a].add(b); A[b].add(a)
    return A
def connected(n,E):
    A=adj(n,E); seen={0}; todo=[0]
    for v in todo:
        for w in A[v]-seen: seen.add(w);todo.append(w)
    return len(seen)==n
def write(name,r):
    (OUT/name).write_text(json.dumps(r,indent=2)+'\n')

# 33: an explicit obstruction to unrestricted identification transfer.
K7={edge(a,b) for a,b in it.combinations(range(7),2)}
G=(K7-{(0,1)})|{(0,7),(1,7)}
def identify(E,a,b):
    mp=lambda x:b if x==a else x
    return {edge(mp(x),mp(y)) for x,y in E if mp(x)!=mp(y)}
assert identify(G,7,0)==K7 and (2,7) not in G
H=identify(G,7,2); assert H==K7-{(0,1)}
r33={'subdivided_graph_edges':sorted(G),'clique_minor_contraction':[7,0],'nonadjacent_identification':[7,2],'result_edges':sorted(H),'result_vertices':7,'result_missing_clique_edge':[0,1],'result_chromatic_number':6,'proof':'A seven-vertex graph has a K7 minor only if it is K7: seven nonempty disjoint branch sets must all be singleton. Identification here gives K7 minus edge 01, hence destroys K7-minor existence. This does not contradict Hadwiger because vertices 0 and 1 can share a color.'}

# 34: test the stated diagnostic, retaining all seed-generated data.
rng=random.Random(34); candidates=[]
for p in [.15,.35,.55]:
    for _ in range(100): candidates.append((f'G12_p{p}',12,{e for e in it.combinations(range(12),2) if rng.random()<p}))
for _ in range(40):
    sizes=[1]*5
    for j in range(7): sizes[rng.randrange(5)]+=1
    group=[g for g,s in enumerate(sizes) for _ in range(s)]
    candidates.append(('C5_independent_blowup',12,{(i,j) for i,j in it.combinations(range(12),2) if (group[i]-group[j])%5 in [1,4]}))
def has_P6(A):
    for S in it.combinations(range(len(A)),6):
        ss=set(S); deg=[len(A[v]&ss) for v in S]
        if sorted(deg)!=[1,1,2,2,2,2]: continue
        seen={S[0]}; todo=[S[0]]
        for v in todo:
            for w in (A[v]&ss)-seen:seen.add(w);todo.append(w)
        if len(seen)==6:return True
    return False
def dominating(A,k):
    full=set(range(len(A)))
    for S in it.combinations(full,k):
        cover=set(S)
        for v in S:cover|=A[v]
        if cover==full:return S
    return None
accepted=[]; filters=co.Counter()
for kind,n,E in candidates:
    if not connected(n,E):filters['disconnected']+=1;continue
    A=adj(n,E)
    if any(all(b in A[a] for a,b in it.combinations(S,2)) for S in it.combinations(range(n),4)): filters['contains_K4']+=1;continue
    if has_P6(A):filters['contains_induced_P6']+=1;continue
    dom=next((s for k in range(1,4) if (s:=dominating(A,k)) is not None),None)
    anti=None
    if dom is None:
        for S in it.combinations(range(n),math.ceil(n/4)):
            bad=set(S)
            for v in S:bad|=A[v]
            rem=set(range(n))-bad
            if len(rem)>=math.ceil(n/4):anti=(S,tuple(sorted(rem)[:math.ceil(n/4)]));break
    accepted.append({'kind':kind,'edges':sorted(E),'dominating_set':dom,'anticomplete_pair':anti,'passes':dom is not None or anti is not None})
r34={'proposed':len(candidates),'filters':dict(filters),'accepted':len(accepted),'domination_size_distribution':dict(co.Counter(len(x['dominating_set']) if x['dominating_set'] else None for x in accepted)),'violations':sum(not x['passes'] for x in accepted),'cases':accepted}

# 35: failed rooting is not an induced-subtree absence certificate.
T={edge(v,(v-1)//2) for v in range(1,15)}
GT=T|{(v,15) for v in range(15)}
assert {e for e in GT if 15 not in e}==T
r35={'tree_edges':sorted(T),'host_edges':sorted(GT),'induced_embedding':list(range(15)),'failed_root':15,'proof':'If tree vertex 0 is sent to universal vertex 15, a vertex at depth two would have to be nonadjacent to 15, which is impossible. Nevertheless vertices 0 through 14 induce the complete binary tree. Thus one failed rooted search is not a certificate of induced-tree absence. The host has clique number and chromatic number three.'}

# 36: exhaustive full-deck lookup for all five-vertex graph isomorphism types.
def canon(n,E):
    pairs=list(it.combinations(range(n),2)); ix={e:i for i,e in enumerate(pairs)}
    return min(sum(1<<ix[edge(p[a],p[b])] for a,b in E) for p in it.permutations(range(n)))
pair5=list(it.combinations(range(5),2)); graphs={}
for mask in range(1<<10):
    E={e for i,e in enumerate(pair5) if mask>>i&1}; c=canon(5,E)
    if c not in graphs:graphs[c]=E
decks=co.defaultdict(list); repeated=0
for c,E in graphs.items():
    cards=[]
    for v in range(5):
        rem=[x for x in range(5) if x!=v];mp={x:i for i,x in enumerate(rem)}
        cards.append(canon(4,{edge(mp[a],mp[b]) for a,b in E if v not in (a,b)}))
    deck=tuple(sorted(cards));decks[deck].append(c)
    if len(set(cards))<5:repeated+=1
r36={'labeled_graphs_tested':1024,'isomorphism_types':len(graphs),'connected_types':sum(connected(5,E) for E in graphs.values()),'distinct_decks':len(decks),'nonisomorphic_deck_collisions':sum(len(v)>1 for v in decks.values()),'types_with_repeated_isomorphic_cards':repeated,'canonical_deck_table':[{'graph_code':c,'edges':sorted(graphs[c]),'deck':d} for d,cs in decks.items() for c in cs]}

# 38: exhaustive oriented circulants, not all digraphs.
circ=[]
for n in range(3,20):
    pairreps=list(range(1,(n+1)//2)); tested=0; admissible=0;best=-1;witness=None
    for choice in it.product((0,1,-1),repeat=len(pairreps)):
        S={a if v==1 else n-a for a,v in zip(pairreps,choice) if v};tested+=1
        if any((-a-b)%n in S for a in S for b in S):continue
        admissible+=1
        if len(S)>best:best=len(S);witness=sorted(S)
    circ.append({'n':n,'oriented_step_sets_tested':tested,'triangle_free_step_sets':admissible,'maximum_outdegree':best,'threshold':math.ceil(n/3),'maximizing_steps':witness})
r38={'range':[3,19],'total_step_sets':sum(x['oriented_step_sets_tested'] for x in circ),'all_below_conjectured_threshold':all(x['maximum_outdegree']<x['threshold'] for x in circ),'orders':circ}

def prism(n):return 2*n,{edge(i,(i+1)%n) for i in range(n)}|{edge(n+i,n+(i+1)%n) for i in range(n)}|{(i,n+i) for i in range(n)}
def perfect_matchings(n,E):
    A=adj(n,E)
    def rec(rem,M):
        if not rem:yield frozenset(M);return
        v=min(rem)
        for w in sorted(A[v]&rem):yield from rec(rem-{v,w},M+[edge(v,w)])
    yield from rec(set(range(n)),[])
def cycles_upto(n,E,L):
    A=adj(n,E);out=set()
    for s in range(n):
        def dfs(path):
            v=path[-1]
            if len(path)>=3 and s in A[v]:out.add(frozenset(edge(path[i],path[(i+1)%len(path)]) for i in range(len(path))))
            if len(path)==L:return
            for w in sorted(A[v]):
                if w>s and w not in path:dfs(path+[w])
        dfs([s])
    return out
def components(n,E):
    A=adj(n,E);seen=set();res=[]
    for s in range(n):
        if s in seen:continue
        todo=[s];seen.add(s)
        for v in todo:
            for w in A[v]-seen:seen.add(w);todo.append(w)
        res.append(todo)
    return res
pr=[]
for n in [10,12,14]:
    N,E=prism(n);C=cycles_upto(N,E,8);count=0;nonham=0;traps=[];dist=co.Counter()
    for M in perfect_matchings(N,E):
        count+=1;k=len(components(N,E-M));dist[k]+=1
        if k==1:continue
        nonham+=1;improve=False
        for c in C:
            if len(c)%2==0 and len(c&M)==len(c)//2 and len(components(N,E-(M^c)))<k:improve=True;break
        if not improve:traps.append({'matching':sorted(M),'complementary_cycles':components(N,E-M)})
    pr.append({'rim_length':n,'vertices':N,'perfect_matchings':count,'cycles_length_at_most_8':len(C),'complement_component_distribution':dict(dist),'nonhamiltonian_complements':nonham,'traps':traps})
r39={'prisms':pr}

# 40: find the promised one-visit Petersen assembly and verify cube obstruction.
V=list(it.combinations(range(5),2)); E={edge(i,j) for i,j in it.combinations(range(10),2) if not set(V[i])&set(V[j])};A=adj(10,E)
rotation=[V.index(tuple(sorted(((a+1)%5,(b+1)%5)))) for a,b in V]
orbits=[];seen=set()
for s in range(10):
    if s in seen:continue
    orb=[];v=s
    while v not in seen:seen.add(v);orb.append(v);v=rotation[v]
    orbits.append(orb)
paths=[]
for orb in orbits:paths.append([p for p in it.permutations(orb) if all(p[i+1] in A[p[i]] for i in range(len(p)-1))])
ham=next(p+q for p in paths[0] for q in paths[1] if q[0] in A[p[-1]])
gray=[0,1,3,2,6,7,5,4];assert all((a^b).bit_count()==1 for a,b in zip(gray,gray[1:]))
r40={'petersen_vertices':V,'petersen_orbits':orbits,'petersen_one_visit_hamiltonian_path':ham,'cube_complement_orbits':[[i,i^7] for i in range(4)],'cube_each_fiber_has_no_edge':all((i^(i^7)).bit_count()==3 for i in range(4)),'cube_global_hamiltonian_path':gray}

# 54: verify every entry of the exact rook-graph baseline and derived blocks.
RV=list(it.product(range(3),repeat=2));root=RV.index((0,0));RA=[[int(i!=j and (RV[i][0]==RV[j][0] or RV[i][1]==RV[j][1])) for j in range(9)] for i in range(9)]
assert all(sum(RA[i])==4 for i in range(9))
assert all(sum(RA[i][k]*RA[k][j] for k in range(9))+RA[i][j]-2*(i==j)==2 for i in range(9) for j in range(9))
N=[j for j in range(9) if RA[root][j]];W=[j for j in range(9) if j!=root and j not in N]
C=[[RA[i][j] for j in W] for i in N];B=[[RA[i][j] for j in W] for i in W];M=[[RA[i][j] for j in N] for i in N]
assert all(sum(C[i][k]*B[k][j] for k in range(4))==2-C[i][j]-sum(M[i][k]*C[k][j] for k in range(4)) for i in range(4) for j in range(4))
r54={'rook_vertices':RV,'rook_adjacency':RA,'rook_matrix_identity_entries_verified':81,'root_neighbors':N,'outside_vertices':W,'C':C,'B':B,'M':M,'derived_99_equations':['B symmetric binary with zero diagonal and B 1 = 12 1','C B = 2 J - C - M C','B^2 + B = 12 I + 2 J - C^T C'],'proof_file':'discrete_restricted_lemmas.txt'}
res={'33':r33,'34':r34,'35':r35,'36':r36,'38':r38,'39':r39,'40':r40,'54':r54};write('discrete_graph_results.json',res)
for k,r in res.items():
    if k=='34':print(k,{a:b for a,b in r.items() if a!='cases'})
    elif k=='36':print(k,{a:b for a,b in r.items() if a!='canonical_deck_table'})
    elif k=='39':print(k,[{a:(len(b) if a=='traps' else b) for a,b in x.items()} for x in r['prisms']])
    elif k=='38':print(k,{a:b for a,b in r.items() if a!='orders'})
    else:print(k,'verified')
