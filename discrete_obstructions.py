import itertools as it, collections as co, pathlib, json, heapq
OUT=pathlib.Path(__file__).parent

# Exhaust the entire proposed single-edge neighborhood after all 100 random
# moves failed: this determines whether sampling or the neighborhood is at fault.
seed=[tuple(3*c+t for t in (x,y,(x+y)%3,(x+2*y)%3)) for c in (0,1) for x,y in it.product(range(3),repeat=2)]
def disjoint(e,f):return all(x!=y for x,y in zip(e,f))
new=[e for e in it.product(range(7),repeat=4) if e not in seed]
counts=co.Counter();minavoiders=[9,9];witnesses=[]
for e in new:
    avoid=[[f for f in seed[9*c:9*(c+1)] if disjoint(e,f)] for c in (0,1)]
    for c in (0,1):minavoiders[c]=min(minavoiders[c],len(avoid[c]))
    assert all(len(x)>=2 for x in avoid)
    counts[(len(avoid[0]),len(avoid[1]))]+=1
    # Verify an explicit three-edge matching after EACH possible deletion.
    for deleted in seed:
        a=next(f for f in avoid[0] if f!=deleted);b=next(f for f in avoid[1] if f!=deleted)
        assert disjoint(a,b) and disjoint(a,e) and disjoint(b,e)
    if len(witnesses)<3:witnesses.append({'added_edge':e,'avoiding_edges_in_copy_zero':avoid[0],'avoiding_edges_in_copy_one':avoid[1]})
r51={'absent_edges_exhausted':len(new),'deletions_per_edge':18,'replacement_hypergraphs_verified':18*len(new),'minimum_avoiding_seed_edges_per_copy':minavoiders,'all_replacements_have_matching_number_exactly':3,'avoidance_count_distribution':[{'copy_zero':a,'copy_one':b,'new_edges':c} for (a,b),c in sorted(counts.items())],'examples':witnesses,'upper_bound_reason':'Removing an edge leaves matching number at most two; adding one edge can increase it by at most one.'}

# Test every unrestricted unit coordinate move at an actual cube trap.
L=json.load(open(OUT/'discrete_landscape_results.json'))
cube=next(x for x in L['53']['graphs'] if x['graph']=='cube');z=tuple(cube['positive_trap_components'][0]['coefficients']);basis=cube['cycle_basis'];E=cube['edges']
def flow(z):return [sum(z[i]*basis[i][j] for i in range(len(z))) for j in range(len(E))]
def potential(z):
    f=flow(z);return sum(v==0 for v in f)+sum(max(0,abs(v)-4) for v in f)
neighbors=[]
for i in range(len(z)):
    for d in (-1,1):
        w=list(z);w[i]+=d;neighbors.append({'coordinate':i,'change':d,'state':w,'potential':potential(w)})
assert potential(z)==1 and all(x['potential']>1 for x in neighbors)
# A short minimax escape in a bounded box supplies an upper witness. Since
# every first move has potential >=2, any path with max potential 2 is globally
# optimal as to barrier height, independently of the box restriction.
best={z:1};prev={};heap=[(1,z)];target=None
while heap:
    cost,s=heapq.heappop(heap)
    if cost!=best[s]:continue
    if potential(s)==0:target=s;break
    for i in range(len(z)):
        for d in (-1,1):
            t=list(s);t[i]+=d;t=tuple(t)
            if any(abs(t[j]-z[j])>2 for j in range(len(z))):continue
            nc=max(cost,potential(t))
            if nc<best.get(t,10**9):best[t]=nc;prev[t]=s;heapq.heappush(heap,(nc,t))
assert target is not None
path=[target]
while path[-1]!=z:path.append(prev[path[-1]])
path.reverse()
r53={'graph':'cube','edge_orientation':'lower vertex label to higher','edges':E,'cycle_basis':basis,'trap_coefficients':z,'trap_flow':flow(z),'trap_potential':1,'all_ten_unrestricted_unit_coordinate_moves':neighbors,'escape_path':[{'coefficients':s,'potential':potential(s),'flow':flow(s)} for s in path],'escape_maximum_potential':max(potential(s) for s in path),'unrestricted_first_move_lower_bound':min(x['potential'] for x in neighbors)}
res={'51':r51,'53':r53};(OUT/'discrete_obstruction_results.json').write_text(json.dumps(res,indent=2)+'\n')
print('51',r51['replacement_hypergraphs_verified'],r51['minimum_avoiding_seed_edges_per_copy'],'all matching number3')
print('53 trap',z,'neighbor potentials',[x['potential'] for x in neighbors],'escape',[x['potential'] for x in r53['escape_path']])
