"""Reproducible finite controls for the analysis/computation work round.

Run with Python 3; standard library only. Claims and scope are in
computation_derivations.txt and computation_work.json.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product, permutations
from functools import lru_cache
from collections import Counter
from math import comb, isqrt
import json, random, time

OUT=Path(__file__).resolve().parent

def canonical(clauses):return tuple(sorted(set(tuple(sorted(c)) for c in clauses)))
def assign(clauses,var,value):
    true=var if value else -var
    return canonical(tuple(l for l in c if l!=-true) for c in clauses if true not in c)
def sat(clauses,mask):return all(any(bool(mask>>(abs(l)-1)&1)==(l>0) for l in c) for c in clauses)

def card82():
    graphs={'K4':(4,list(combinations(range(4),2))),
            'K3,3':(6,[(a,b) for a in range(3) for b in range(3,6)]),
            'cube':(8,[(a,b) for a in range(8) for b in range(a+1,8) if (a^b).bit_count()==1])}
    result={}
    for name,(n,edges) in graphs.items():
        clauses=[]
        for v in range(n):
            incident=[i+1 for i,e in enumerate(edges) if v in e]
            for bits in product((0,1),repeat=3):
                if sum(bits)%2 != int(v==0):
                    clauses.append(tuple(-i if b else i for i,b in zip(incident,bits)))
        clauses=canonical(clauses)
        @lru_cache(None)
        def proof(cnf):
            if () in cnf:return False,1
            if not cnf:return True,1
            var=min(abs(l) for c in cnf for l in c)
            lo,ls=proof(assign(cnf,var,False));hi,hs=proof(assign(cnf,var,True))
            return lo or hi,1+ls+hs
        value,tree=proof(clauses)
        count=sum(sat(clauses,m) for m in range(1<<len(edges)))
        assert count==0 and not value
        result[name]={'vertices':n,'edges':edges,'clauses':clauses,'assignments_checked':1<<len(edges),
                      'satisfying_assignments':count,'unshared_tree_nodes':tree,'shared_distinct_residuals':proof.cache_info().currsize}
    return result

def reachable(n,edges,start):
    seen={start};todo=[start]
    while todo:
        v=todo.pop()
        for a,b in edges:
            if a==v and b not in seen:seen.add(b);todo.append(b)
    return seen

def card83():
    for blocks in product(range(16),repeat=2):
        edges=[];mask=1
        for layer,block in enumerate(blocks):
            edges += [(2*layer+i,2*(layer+1)+j) for i,j in product(range(2),repeat=2) if block>>(2*i+j)&1]
            mask=sum(int(any((mask>>i&1) and (block>>(2*i+j)&1) for i in range(2)))<<j for j in range(2))
        expected=sum(int(4+j in reachable(6,edges,0))<<j for j in range(2))
        assert mask==expected
    possible=[(a,b) for a in range(4) for b in range(4) if a!=b]
    mismatches=0;witness=None
    for m in range(1<<len(possible)):
        edges=[e for i,e in enumerate(possible) if m>>i&1]
        projected=(0,3) in edges
        actual=3 in reachable(4,edges,0)
        if projected!=actual:
            mismatches+=1
            if witness is None or len(edges)<len(witness):witness=edges
    return {'layered_instances':256,'layered_mismatches':0,'all_four_vertex_digraphs':4096,
            'outside_promise_projection_mismatches':mismatches,'smallest_found_witness':witness,
            'frontier_working_bits':'two reachability bits, two next-frontier bits, constant local indices, and O(log layers) input position'}

def card84():
    rows=[]
    for eps in (F(1),F(1,2),F(1,4),F(1,16),F(0)):
        for b in (4,8,12):
            v=[F(1),F(0),F(0),F(0)];step_rows=[];bound=F(0)
            for t in range(1,17):
                w=[(1-eps)*x+eps/4 for x in v]
                v=[F((x*(1<<b)).numerator//(x*(1<<b)).denominator,1<<b) for x in w[:3]]
                v.append(1-sum(v))
                exact=[F(1,4)+(F(3,4) if j==0 else F(-1,4))*(1-eps)**t for j in range(4)]
                tv=sum(abs(x-y) for x,y in zip(v,exact))/2
                error=abs(v[0]-exact[0]);bound=(1-eps)*bound+F(3,1<<b)
                assert error<=tv<=bound
                step_rows.append({'t':t,'acceptance_error':str(error),'tv':str(tv),'bound':str(bound)})
            rows.append({'epsilon':str(eps),'b':b,'steps':step_rows,'max_acceptance_error':str(max(F(x['acceptance_error']) for x in step_rows))})
    return {'configurations':15,'step_checks':240,'rows':rows}

class BDD:
    def __init__(self):self.nodes={0:None,1:None};self.unique={};self.app={};self.quant_cache={}
    def make(self,var,lo,hi):
        if lo==hi:return lo
        key=(var,lo,hi)
        if key not in self.unique:
            idx=len(self.nodes);self.unique[key]=idx;self.nodes[idx]=key
        return self.unique[key]
    def build(self,vals,var=0):
        if all(v==vals[0] for v in vals):return int(vals[0])
        return self.make(var,self.build(vals[0::2],var+1),self.build(vals[1::2],var+1))
    def apply(self,op,u,v):
        key=(op,min(u,v),max(u,v))
        if key in self.app:return self.app[key]
        if u<2 and v<2:ans=int(bool(u or v) if op=='or' else bool(u and v))
        else:
            vu=self.nodes[u][0] if u>=2 else 100
            vv=self.nodes[v][0] if v>=2 else 100
            var=min(vu,vv)
            ul,uh=self.nodes[u][1:] if vu==var else (u,u)
            vl,vh=self.nodes[v][1:] if vv==var else (v,v)
            ans=self.make(var,self.apply(op,ul,vl),self.apply(op,uh,vh))
        self.app[key]=ans;return ans
    def quant(self,node,var,op):
        key=(node,var,op)
        if key in self.quant_cache:return self.quant_cache[key]
        if node<2:ans=node
        else:
            x,lo,hi=self.nodes[node]
            ans=self.apply(op,lo,hi) if x==var else self.make(x,self.quant(lo,var,op),self.quant(hi,var,op))
        self.quant_cache[key]=ans;return ans
    def evaluate(self,node,mask):
        while node>=2:
            v,lo,hi=self.nodes[node];node=hi if mask>>v&1 else lo
        return bool(node)
    def size(self,node):
        seen=set();todo=[node]
        while todo:
            x=todo.pop()
            if x not in seen:
                seen.add(x)
                if x>=2:todo.extend(self.nodes[x][1:])
        return len(seen)

def clause_population(n):
    return [tuple(v if s else -v for v,s in zip(vs,signs)) for vs in combinations(range(1,n+1),3) for signs in product((0,1),repeat=3)]

def card85():
    rng=random.Random(85);population=clause_population(6);records=[];checks=0
    for start_exists in (True,False):
        for case in range(100):
            clauses=canonical(rng.sample(population,8));vals=[sat(clauses,m) for m in range(64)]
            manager=BDD();node=manager.build(vals);sizes=[manager.size(node)]
            for var in range(5,-1,-1):
                exists=(var%2==0)==start_exists;op='or' if exists else 'and'
                node=manager.quant(node,var,op);half=len(vals)//2
                vals=[(a or b) if exists else (a and b) for a,b in zip(vals[:half],vals[half:])]
                assert all(manager.evaluate(node,m)==v for m,v in enumerate(vals));checks+=len(vals)
                sizes.append(manager.size(node))
            records.append({'prefix_start':'exists' if start_exists else 'forall','case':case,'clauses':clauses,'node_counts_including_terminals':sizes,'truth':bool(node)})
    return {'formulas':200,'intermediate_truth_entry_checks':checks,'max_reachable_nodes':max(max(r['node_counts_including_terminals']) for r in records),'records':records}

def padd(a,b,sign=1):
    result=a.copy()
    for m,c in b.items():result[m]=result.get(m,0)+sign*c
    return {m:c for m,c in result.items() if c}
def pmul(a,b):
    result={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            m=tuple(x+y for x,y in zip(ma,mb));result[m]=result.get(m,0)+ca*cb
    return {m:c for m,c in result.items() if c}

def card87():
    rng=random.Random(87);common={(0,0,0,0):1,(1,0,0,0):1};records=[]
    def term():
        p=common.copy();factors=[]
        for _ in range(5):
            coeff=(0,0,0,0)
            while not any(coeff):coeff=tuple(rng.choice((-1,0,1)) for _ in range(4))
            factors.append(coeff)
            linear={tuple(int(i==j) for i in range(4)):c for j,c in enumerate(coeff) if c}
            p=pmul(p,linear)
        return p,factors
    for case in range(100):
        terms=[term() for _ in range(3)];poly={}
        for p,_ in terms:poly=padd(poly,p)
        for label,p in (('sum',poly),('cancellation',padd(terms[0][0],terms[0][0],-1))):
            u={}
            for m,c in p.items():
                assert sum(m)<=6 and max(m)<=6
                power=sum(v*7**i for i,v in enumerate(m))
                assert power not in u;u[power]=c
            assert bool(p)==bool(u)
            records.append({'case':case,'kind':label,'factors':[x[1] for x in terms] if label=='sum' else None,'terms':len(p),'degree':max(u,default=-1),'is_zero':not bool(p)})
    return {'polynomials':200,'zero_cases':sum(x['is_zero'] for x in records),'max_substituted_degree':max(x['degree'] for x in records),'records':records}

def card88():
    rows=[]
    for k in range(1,7):
        indices=list(product(range(k+1),repeat=2));matrix=[]
        for a,b in indices:
            row=[comb(k,a)*comb(k,b) if a+c==k and b+d==k else 0 for c,d in indices]
            assert sum(x!=0 for x in row)==1;matrix.append(row)
        assert all(sum(row[j]!=0 for row in matrix)==1 for j in range(len(indices)))
        rank=len(indices);mult=k.bit_length()-1+k.bit_count()-1;gates=3+2*mult
        rows.append({'k':k,'rank':rank,'gates':gates,'rank_le_gates':rank<=gates,'log2rank_le_gates':rank<=2**gates})
    return {'rows':rows,'proof':'The coefficient matrix has one nonzero entry in every row and column, hence full rank (k+1)^2.'}

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def card89():
    rng=random.Random(89);primes=[n for n in range(128,256) if prime(n)];records=[]
    for case in range(50):
        p,q=rng.sample(primes,2);N=p*q;rows=[]
        for t in (1,2,4,6):
            prefix=p>>(8-t);candidates=list(range(prefix<<(8-t),(prefix+1)<<(8-t)))
            candidates=[d for d in candidates if d%2];all_candidates=[]
            for pref in range(1<<(t-1),1<<t):
                all_candidates += [d for d in range(pref<<(8-t),(pref+1)<<(8-t)) if d%2]
            assert p in candidates and sorted(all_candidates)==list(range(129,256,2))
            rows.append({'revealed_bits':t,'prefix':prefix,'known_prefix_candidates':len(candidates),'all_prefix_candidates':len(all_candidates),'divisors_in_known_prefix':[d for d in candidates if N%d==0]})
        records.append({'case':case,'p':p,'q':q,'N':N,'rows':rows})
    return {'semiprimes':50,'factor_bits':8,'known_prefix_counts':[64,32,8,2],'all_prefix_counts':[64,64,64,64],'records':records}

def graph90(kind):
    coords=list(product(range(4),repeat=2));adj=[set() for _ in coords]
    steps={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    for i,(a,b) in enumerate(coords):
        for j,(c,d) in enumerate(coords):
            if i!=j and ((a==c or b==d) if kind=='rook' else ((c-a)%4,(d-b)%4) in steps):adj[i].add(j)
    return adj
def signature90(adj):
    hist=Counter()
    for a in range(16):
        for b in adj[a]:
            if a<b:
                common=adj[a]&adj[b]
                hist[sum(v in adj[u] for u,v in combinations(sorted(common),2))]+=1
    return dict(hist)
def card90():
    rng=random.Random(90);results={}
    for kind in ('rook','shrikhande'):
        adj=graph90(kind);sig=signature90(adj)
        assert all(len(a)==6 for a in adj)
        assert all(len(adj[i]&adj[j])==2 for i,j in combinations(range(16),2))
        for _ in range(100):
            perm=list(range(16));rng.shuffle(perm);new=[set() for _ in range(16)]
            for i in range(16):new[perm[i]]={perm[j] for j in adj[i]}
            assert signature90(new)==sig
        results[kind]={'degree':6,'common_neighbors_each_distinct_pair':2,'edge_common_neighbor_induced_edges':sig,'relabelings_checked':100}
    return results

def card91():
    rng=random.Random(91);perms=list(permutations(range(3)));records=[]
    for graph in ('C8','K8'):
        edges=sorted([(i,i+1) for i in range(7)]+[(0,7)]) if graph=='C8' else list(combinations(range(8),2))
        for mode in ('identity','cyclic','arbitrary'):
            for case in range(4):
                maps=[]
                for edge in edges:
                    if mode=='identity':perm=(0,1,2)
                    elif mode=='cyclic':
                        shift=rng.randrange(3);perm=tuple((a+shift)%3 for a in range(3))
                    else:perm=rng.choice(perms)
                    maps.append(perm)
                best=-1;witness=None
                for labels in product(range(3),repeat=8):
                    score=sum(p[labels[u]]==labels[v] for (u,v),p in zip(edges,maps))
                    if score>best:best=score;witness=labels
                row={'graph':graph,'mode':mode,'case':case,'constraints':[[u,v,list(p)] for (u,v),p in zip(edges,maps)],'satisfied':best,'total':len(edges),'witness':witness}
                if graph=='C8':
                    lookup=dict(zip(edges,maps));composition=[]
                    for a in range(3):
                        current=a
                        for i in range(7):current=lookup[(i,i+1)][current]
                        current=lookup[(0,7)].index(current);composition.append(current)
                    predicted=8 if any(a==b for a,b in enumerate(composition)) else 7
                    assert best==predicted;row['cycle_composition']=composition
                records.append(row)
    return {'instances':24,'assignments_per_instance':6561,'records':records}

def card92():
    # Commuting four-projector control; diagonal entries indexed by bit strings.
    rows=[]
    for bits in product((0,1),repeat=4):
        old=sum(bits);new=sum(1-(1-bits[i])*(1-bits[j])*(1-bits[i]) for i in range(4) for j in range(4) if i!=j)
        assert new==old*(8-old-1) and F(new,12)>=F(old,4)
        rows.append({'bits':bits,'old_energy':old,'new_energy':new,'old_density':str(F(old,4)),'new_density':str(F(new,12))})
    return {'basis_states_checked':16,'old_normalized_gap':'1/4','new_normalized_gap':'1/2','old_terms':4,'new_terms':12,'new_locality':2,'rows':rows}

def propagate(cnf,remaining):
    while True:
        if () in cnf:return cnf,remaining
        units=[c[0] for c in cnf if len(c)==1]
        if not units:return cnf,remaining
        lit=min(units,key=lambda x:(abs(x),x>0));var=abs(lit)
        cnf=assign(cnf,var,lit>0);remaining=remaining-{var}

def card94():
    rng=random.Random(94);population=clause_population(8);records=[];counterexamples={};aggregate={}
    for case in range(500):
        original=canonical(rng.sample(population,12));truth=any(sat(original,m) for m in range(256));per_rules={}
        for rule in ('least','most_occurrences'):
            calls=0;branch_count=0;increases=Counter();max_changes={str(a):None for a in (F(0),F(1,4),F(1,2))}
            def solve(cnf,remaining,parent_potential=None,parent_snapshot=None):
                nonlocal calls,branch_count
                calls+=1;cnf,remaining=propagate(cnf,remaining)
                m2=sum(len(c)==2 for c in cnf)
                potential={str(a):F(len(remaining))+a*m2 for a in (F(0),F(1,4),F(1,2))}
                if parent_potential is not None:
                    for alpha,value in potential.items():
                        delta=value-parent_potential[alpha]
                        if max_changes[alpha] is None or delta>max_changes[alpha]:max_changes[alpha]=delta
                        if delta>0:
                            increases[alpha]+=1
                            counterexamples.setdefault(alpha,{'case':case,'rule':rule,'original':original,'parent':parent_snapshot,'child_clauses':cnf,'child_remaining':sorted(remaining),'delta':str(delta)})
                if () in cnf:return False
                if not cnf:return True
                counts=Counter(abs(l) for c in cnf for l in c)
                var=min(counts) if rule=='least' else min(counts,key=lambda v:(-counts[v],v));branch_count+=1
                snapshot={'clauses':cnf,'remaining':sorted(remaining),'branch_variable':var}
                for value in (False,True):
                    if solve(assign(cnf,var,value),remaining-{var},potential,snapshot):return True
                return False
            decision=solve(original,frozenset(range(1,9)));assert decision==truth
            per_rules[rule]={'calls':calls,'branches':branch_count,'positive_potential_changes':dict(increases),'max_potential_changes':{a:None if v is None else str(v) for a,v in max_changes.items()}}
        records.append({'case':case,'clauses':original,'satisfiable':truth,'rules':per_rules})
    for rule in ('least','most_occurrences'):
        aggregate[rule]={'total_calls':sum(r['rules'][rule]['calls'] for r in records),'max_calls':max(r['rules'][rule]['calls'] for r in records)}
    return {'formulas':500,'decision_checks':1000,'aggregate':aggregate,'positive_change_witnesses':counterexamples,'records':records}

def signed_statistics(n,k,rng):
    adj=[0]*n
    for i in range(n):
        bits=rng.getrandbits(n-i-1)<<(i+1);adj[i]|=bits
        while bits:
            b=bits&-bits;j=b.bit_length()-1;adj[j]|=1<<i;bits-=b
    planted=sorted(rng.sample(range(n),k)) if k else []
    for i,j in combinations(planted,2):adj[i]|=1<<j;adj[j]|=1<<i
    degrees=[x.bit_count() for x in adj];edges=sum(degrees)//2;tri_edge_sum=0
    for i in range(n):
        bits=adj[i]&~((1<<(i+1))-1)
        while bits:
            b=bits&-bits;j=b.bit_length()-1;tri_edge_sum+=(adj[i]&adj[j]).bit_count();bits-=b
    assert tri_edge_sum%3==0;triangles=tri_edge_sum//3
    E=2*edges-comb(n,2);T=8*triangles-4*sum(comb(d,2) for d in degrees)+2*(n-2)*edges-comb(n,3)
    if n<=8:
        def sign(i,j):return 1 if adj[i]>>j&1 else -1
        assert E==sum(sign(i,j) for i,j in combinations(range(n),2))
        assert T==sum(sign(i,j)*sign(j,k)*sign(k,i) for i,j,k in combinations(range(n),3))
    return {'E':E,'T':T,'planted':planted}

def card95():
    train=random.Random(95);test=random.Random(1095);rows=[]
    # Direct cubic-product checks validate the counting identity on eight
    # separate small control graphs, apart from the 480 benchmark graphs.
    for k in (0,3):
        for seed in range(4):signed_statistics(8,k,random.Random(seed))
    assert 8*comb(8,3)-4*8*comb(7,2)+2*6*comb(8,2)-comb(8,3)==comb(8,3)
    for n in (64,128,256):
        low=0
        while (low+1)**5<=n*n:low+=1
        for k in (low,isqrt(n)):
            data={}
            for split,rng in (('train',train),('test',test)):
                data[split]=[{'label':label,**signed_statistics(n,k if label else 0,rng)} for label in (0,1) for _ in range(20)]
            stats={}
            for name in ('E','T'):
                values=sorted({r[name] for r in data['train']});thresholds=values+[values[-1]+1]
                threshold=min(thresholds,key=lambda t:(-sum((r[name]>=t)==bool(r['label']) for r in data['train']),t))
                counts=Counter(('TP' if r['label'] else 'FP') if r[name]>=threshold else ('FN' if r['label'] else 'TN') for r in data['test'])
                for key in ('TP','TN','FP','FN'):counts[key]+=0
                stats[name]={'threshold':threshold,'test_confusion':dict(counts),'test_correct':counts['TP']+counts['TN'],'test_total':40}
            rows.append({'n':n,'k':k,'statistics':stats,'data':data,'null_edge_variance':comb(n,2),'null_triangle_variance':comb(n,3),'planted_edge_mean':comb(k,2),'planted_triangle_mean':comb(k,3)})
    return {'settings':6,'graphs':480,'small_graph_identity_controls':8,'threshold_tie_rule':'smallest integer threshold among training-accuracy maximizers','rows':rows}

def card96():
    rows=[]
    for N in (1,2,4,8,16):
        moduli_sum=sum((F(1,2**(j+1)) for j in range(N)),F(0))
        assert moduli_sum==1-F(1,2**N)
        rows.append({'N':N,'sum_moduli':str(moduli_sum),'radius':'exp(-2*pi*'+str(moduli_sum)+')'})
    return {'positive_moduli':'m_j=2^(-j-1), j>=0','limiting_radius':'exp(-2*pi)>0','rows':rows,'precise_source':'https://arxiv.org/html/2309.02107v2#S1.SS2'}

def card97():
    rows=[];counts=Counter()
    for m in (4,6,8):
        for a,b in product(range(-2,3),repeat=2):
            real=F(-3,4)+F(a,2**m);imag=F(b,2**m)
            A=1-4*real;B=-4*imag;norm2=A*A+B*B;L=norm2-2*A
            assert A>0 and L>0
            fixed=L*L<4*norm2
            two=16*((real+1)**2+imag**2)<1 and (real,imag)!=(F(-3,4),F(0))
            assert not(fixed and two)
            label='attracting_fixed' if fixed else 'attracting_two_cycle' if two else 'unclassified'
            counts[label]+=1
            rows.append({'m':m,'a':a,'b':b,'c_real':str(real),'c_imag':str(imag),'classification':label,'fixed_inequality_margin':str(4*norm2-L*L),'two_cycle_squared_multiplier':str(16*((real+1)**2+imag**2))})
    return {'grid_entries':75,'counts':dict(counts),'rows':rows}

def card98():
    rows=[]
    for N in (100,1000,10000,100000,1000000):
        orbit=set();p=1
        while p<=N:
            q=p
            while q<=N:orbit.add(q);q*=3
            p*=2
        rows.append({'N':N,'positive_orbit_count':len(orbit),'symmetric_orbit_density':str(F(2*len(orbit),2*N+1)),'orbit':sorted(orbit)})
    return {'frequency_orbit':'{2^a*3^b:a,b>=0}','rows':rows,'consequence':'An invariant nonzero coefficient contributes only O((log N)^2/N) to the Cesaro mean, which does not contradict its nonatomic limit zero.'}

def card99():
    rows=[];counts=Counter()
    for alpha,p in product((F(3,2),F(19,10),F(199,100),F(2)),(F(7,2),F(39,10),F(4),F(41,10))):
        beta=2+p*(1/alpha-1);kind='convergent' if beta>0 else 'log_divergent' if beta==0 else 'power_divergent';counts[kind]+=1
        vals=[]
        for j in range(1,7):
            form=f'({alpha})^(1-({p}))*'+(f'({j})*log(10)' if beta==0 else f'(1-10^(-({j})*({beta})))/({beta})')
            vals.append({'j':j,'exact_I_over_pi':form})
        rows.append({'alpha':str(alpha),'p':str(p),'beta':str(beta),'classification':kind,'values':vals})
    return {'models':16,'exact_cutoff_expressions':96,'counts':dict(counts),'rows':rows}

if __name__=='__main__':
    all_results={}
    for number in (82,83,84,85,87,88,89,90,91,92,94,95,96,97,98,99):
        start=time.monotonic();result=globals()['card'+str(number)]();result['execution_seconds']=round(time.monotonic()-start,6)
        all_results[str(number)]=result
        (OUT/'computation_batch_results.json').write_text(json.dumps(all_results,indent=2)+'\n')
        summary={k:v for k,v in result.items() if k not in ('rows','records','data')}
        if number in (82,90):summary={k:{z:y for z,y in v.items() if z not in ('clauses','edges')} if isinstance(v,dict) else v for k,v in result.items()}
        print(json.dumps({'id':number,'summary':summary}),flush=True)
