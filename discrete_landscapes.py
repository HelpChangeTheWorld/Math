import itertools as it, collections as co, random, json, pathlib
OUT=pathlib.Path(__file__).parent
def landscape(P,neighbors):
    n=len(P);seen=bytearray(n);traps=[];plateaus=0;longest=0;longest_state=None
    for s in range(n):
        if seen[s]:continue
        plateaus+=1;seen[s]=1;todo=[s];boundary=[]
        for v in todo:
            lower=False
            for w in neighbors(v):
                if P[w]<P[v]:lower=True
                elif P[w]==P[v] and not seen[w]:seen[w]=1;todo.append(w)
            if lower:boundary.append(v)
        if P[s]==0:continue
        if not boundary:traps.append({'potential':P[s],'size':len(todo),'state_index':s});continue
        dist={v:0 for v in boundary};queue=list(boundary)
        for v in queue:
            for w in neighbors(v):
                if P[w]==P[v] and w not in dist:dist[w]=dist[v]+1;queue.append(w)
        w=max(dist,key=dist.get);escape=dist[w]+1
        if escape>longest:longest=escape;longest_state=w
    reachable=bytearray(n);queue=[]
    for i,p in enumerate(P):
        if p==0:reachable[i]=1;queue.append(i)
    for v in queue:
        for w in neighbors(v):
            if not reachable[w] and P[w]>=P[v]:reachable[w]=1;queue.append(w)
    return {'states':n,'potential_distribution':dict(sorted(co.Counter(P).items())),'constant_potential_components':plateaus,'positive_trap_components':traps,'states_reaching_zero_without_increase':sum(reachable),'maximum_finite_first_descent_length':longest,'longest_descent_witness_index':longest_state}

def rank(vectors):
    pivot={}
    for x in vectors:
        while x:
            p=x.bit_length()-1
            if p in pivot:x^=pivot[p]
            else:pivot[p]=x;break
    return len(pivot)
rng=random.Random(41);bases=[]
while len(bases)<4:
    b=rng.sample(range(1,16),4)
    if rank(b)==4:bases.append(b)
perms=list(it.permutations(range(4)));ix={p:i for i,p in enumerate(perms)};swaps=list(it.combinations(range(4),2))
trans=[]
for p in perms:
    row=[]
    for a,b in swaps:
        q=list(p);q[a],q[b]=q[b],q[a];row.append(ix[tuple(q)])
    trans.append(row)
states=list(it.product(range(24),repeat=3));P=[]
for p,q,r in states:
    P.append(sum(4-rank([bases[0][j],bases[1][perms[p][j]],bases[2][perms[q][j]],bases[3][perms[r][j]]]) for j in range(4)))
def rota_neighbors(i):
    p,q,r=states[i]
    for t in range(6):
        yield trans[p][t]*576+q*24+r
        yield p*576+trans[q][t]*24+r
        yield p*576+q*24+trans[r][t]
        # Swap row zero, then globally normalize its column order again.
        yield trans[p][t]*576+trans[q][t]*24+trans[r][t]
r41=landscape(P,rota_neighbors);r41['binary_bases_as_bitmasks']=bases;r41['column_normalization']='First row fixed; all simultaneous column permutations are quotiented out, preserving potential and every row-swap move.'
zi=next(i for i,p in enumerate(P) if p==0)
r41['zero_defect_rows']=[bases[0]]+[[bases[k+1][j] for j in perms[states[zi][k]]] for k in range(3)]
if r41['longest_descent_witness_index'] is not None:r41['longest_descent_row_permutations']=[perms[j] for j in states[r41['longest_descent_witness_index']]]

latin=[]
for n in [5,7]:
    states=[]
    for missr in range(n):
        rows=[i for i in range(n) if i!=missr]
        for missc in range(n):
            cols=[j for j in range(n) if j!=missc]
            for p in it.permutations(cols):
                if len({(i+j)%n for i,j in zip(rows,p)})==n-1:states.append(frozenset(i*n+j for i,j in zip(rows,p)))
    ix={s:i for i,s in enumerate(states)}
    def ns(s):
        for removed in s:
            t=s-{removed};usedr={x//n for x in t};usedc={x%n for x in t};useds={(x//n+x%n)%n for x in t}
            for r in set(range(n))-usedr:
                for c in set(range(n))-usedc:
                    cell=r*n+c
                    if cell!=removed and (r+c)%n not in useds:yield ix[frozenset(t|{cell})]
    goals=[]
    for i,s in enumerate(states):
        mr=next(iter(set(range(n))-{x//n for x in s}));mc=next(iter(set(range(n))-{x%n for x in s}));used={(x//n+x%n)%n for x in s}
        if (mr+mc)%n not in used:goals.append(i)
    dist={i:0 for i in goals};queue=list(goals);parent={}
    for i in queue:
        for j in ns(states[i]):
            if j not in dist:dist[j]=dist[i]+1;parent[j]=i;queue.append(j)
    worst=max(dist,key=dist.get);path=[worst]
    while path[-1] in parent:path.append(parent[path[-1]])
    latin.append({'n':n,'candidate_state_budget':n*n*__import__('math').factorial(n-1),'valid_partial_transversals':len(states),'directly_augmentable':len(goals),'unreachable_states':len(states)-len(dist),'distance_distribution':dict(sorted(co.Counter(dist.values()).items())),'maximum_distance':dist[worst],'longest_exchange_path':[[[x//n,x%n] for x in sorted(states[j])] for j in path]})
r52={'cyclic_squares':latin}

def edge(a,b):return (min(a,b),max(a,b))
def prism(n):return 2*n,{edge(i,(i+1)%n) for i in range(n)}|{edge(n+i,n+(i+1)%n) for i in range(n)}|{(i,n+i) for i in range(n)}
pv=list(it.combinations(range(5),2));petersen={edge(i,j) for i,j in it.combinations(range(10),2) if not set(pv[i])&set(pv[j])}
cube={edge(i,j) for i,j in it.combinations(range(8),2) if (i^j).bit_count()==1}
inputs=[('Petersen',10,petersen),('cube',8,cube)]+[(f'prism_{n}',*prism(n)) for n in [5,6]]
flows=[]
for name,n,E in inputs:
    edges=sorted(E);eix={e:i for i,e in enumerate(edges)};A=[set() for _ in range(n)]
    for a,b in E:A[a].add(b);A[b].add(a)
    seen={0};todo=[0];tree=set()
    for v in todo:
        for w in sorted(A[v]):
            if w not in seen:seen.add(w);todo.append(w);tree.add(edge(v,w))
    TA=[set() for _ in range(n)]
    for a,b in tree:TA[a].add(b);TA[b].add(a)
    basis=[]
    for a,b in edges:
        if (a,b) in tree:continue
        prev={b:None};q=[b]
        for v in q:
            for w in sorted(TA[v]):
                if w not in prev:prev[w]=v;q.append(w)
        path=[a]
        while path[-1]!=b:path.append(prev[path[-1]])
        path=path[::-1];vec=[0]*len(edges);vec[eix[(a,b)]]=1
        for u,v in zip(path,path[1:]):vec[eix[edge(u,v)]]+=1 if u<v else -1
        div=[0]*n
        for (u,v),f in zip(edges,vec):div[u]+=f;div[v]-=f
        assert not any(div);basis.append(vec)
    beta=len(basis);coeffs=list(it.product(range(-2,3),repeat=beta));powers=[5**(beta-1-i) for i in range(beta)];pot=[];firstflow=None
    for z in coeffs:
        f=[sum(z[i]*basis[i][e] for i in range(beta)) for e in range(len(edges))]
        p=sum(v==0 for v in f)+sum(max(0,abs(v)-4) for v in f);pot.append(p)
        if p==0 and firstflow is None:firstflow=f
    def ns(i):
        for d,power in enumerate(powers):
            z=coeffs[i][d]
            if z>-2:yield i-power
            if z<2:yield i+power
    result=landscape(pot,ns);result.update({'graph':name,'vertices':n,'edges':edges,'cycle_rank':beta,'cycle_basis':basis,'one_verified_flow':firstflow})
    if firstflow is not None:
        div=[0]*n
        for (u,v),f in zip(edges,firstflow):assert 1<=abs(f)<=4;div[u]+=f;div[v]-=f
        assert not any(div)
    for t in result['positive_trap_components']:t['coefficients']=coeffs[t['state_index']]
    flows.append(result)
r53={'graphs':flows}
res={'41':r41,'52':r52,'53':r53};(OUT/'discrete_landscape_results.json').write_text(json.dumps(res,indent=2)+'\n')
print('41',{k:v for k,v in r41.items() if k not in ['positive_trap_components','potential_distribution']},'traps',len(r41['positive_trap_components']))
print('52',[{k:v for k,v in x.items() if k!='longest_exchange_path'} for x in latin])
print('53',[{'graph':x['graph'],'states':x['states'],'zero_states':x['potential_distribution'].get(0,0),'trap_components':len(x['positive_trap_components']),'monotone_reachable':x['states_reaching_zero_without_increase'],'max_descent':x['maximum_finite_first_descent_length']} for x in flows])
