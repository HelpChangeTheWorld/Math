"""Exact finite controls for cards 86, 93, and 100; Python standard library only."""
from functools import lru_cache
from itertools import combinations
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent

def oracle(mode):
    @lru_cache(None)
    def dp(handles, secrets, depth, used_leak):
        best=(1, {'guess':min(secrets)})
        if depth==0:
            return best
        def choose(score,tree):
            nonlocal best
            if score>best[0]: best=(score,tree)
        for i in range(len(handles)):
            for j in range(len(handles)):
                for op in ('add','subtract'):
                    sign=1 if op=='add' else -1
                    h=tuple((handles[i][k]+sign*handles[j][k])%7 for k in (0,1))
                    score,tree=dp(handles+(h,),secrets,depth-1,used_leak)
                    choose(score,{'op':op,'handles':[i,j],'next':tree})
                yes=tuple(x for x in secrets if (handles[i][0]*x+handles[i][1]-handles[j][0]*x-handles[j][1])%7==0)
                no=tuple(x for x in secrets if x not in yes)
                score=0; branches={}
                for bit,subset in ((0,no),(1,yes)):
                    if subset:
                        s,t=dp(handles,subset,depth-1,used_leak);score+=s;branches[str(bit)]=t
                choose(score,{'op':'equality','handles':[i,j],'branches':branches})
        if mode!='baseline' and not used_leak:
            groups={}
            for x in secrets:
                bit=x%2 if mode=='parity' else (2%2)
                groups.setdefault(bit,[]).append(x)
            score=0;branches={}
            for bit,subset in sorted(groups.items()):
                s,t=dp(handles,tuple(subset),depth-1,True);score+=s;branches[str(bit)]=t
            choose(score,{'op':'parity' if mode=='parity' else 'copied_handle_index_bit','handle':2,'branches':branches})
        return best
    score,tree=dp(((0,0),(0,1),(1,0)),tuple(range(7)),2,False)
    return {'successful_secrets':score,'probability':str(F(score,7)),'strategy':tree,'cached_states':dp.cache_info().currsize}

def oracle_verify(tree,x):
    h=[0,1,x]
    while 'guess' not in tree:
        op=tree['op']
        if op in ('add','subtract'):
            i,j=tree['handles'];h.append((h[i]+(1 if op=='add' else -1)*h[j])%7);tree=tree['next']
        else:
            if op=='equality':
                i,j=tree['handles'];b=int(h[i]==h[j])
            elif op=='parity':b=x%2
            else:b=tree['handle']%2
            tree=tree['branches'][str(b)]
    return tree['guess']==x

U=[(1,0,0,1),(0,0,1,1),(1,0,0,0),(0,0,0,1),(1,1,0,0),(-1,0,1,0),(0,1,0,-1)]
V=[(1,0,0,1),(1,0,0,0),(0,1,0,-1),(-1,0,1,0),(0,0,0,1),(1,1,0,0),(0,0,1,1)]
W=[(1,0,0,1),(0,0,1,-1),(0,1,0,1),(1,0,1,0),(-1,1,0,0),(0,0,0,1),(1,0,0,0)]

def kron(x,y):return tuple(a*b for a in x for b in y)
def rank3(a,b,c):
    # Every pair of factor vectors is independent. Pick a nonzero 2x2 minor.
    for i,j in combinations(range(len(a)),2):
        det=a[i]*b[j]-a[j]*b[i]
        if det:
            an=c[i]*b[j]-c[j]*b[i]
            bn=a[i]*c[j]-a[j]*c[i]
            return 2 if all(det*c[k]==an*a[k]+bn*b[k] for k in range(len(a))) else 3
    raise AssertionError('Unexpected proportional factors')

def strassen_screen():
    # Coefficientwise verification of the ordered seven-term identity.
    for i in range(4):
        for j in range(4):
            for k in range(4):
                actual=sum(U[t][i]*V[t][j]*W[t][k] for t in range(7))
                expected=int(i//2==k//2 and j%2==k%2 and i%2==j//2)
                assert actual==expected
    factors=[[kron(mode[i],mode[j]) for i in range(7) for j in range(7)] for mode in (U,V,W)]
    # Three pairwise nonproportional rank-one matrices are independent if both
    # factor triples have pairwise independent members. Thus each mode's
    # flattening rank equals the rank of its three factor vectors.
    histogram=Counter();eligible=[]
    for ids in combinations(range(49),3):
        ranks=tuple(rank3(*(mode[i] for i in ids)) for mode in factors)
        histogram[ranks]+=1
        if max(ranks)<=2:eligible.append(ids)
    return {'term_order':'7*i+j, with i,j zero-based in the U,V,W arrays in this script',
            'seven_term_identity_coefficient_checks':64,'triples_screened':sum(histogram.values()),
            'rank_histogram':{str(k):v for k,v in sorted(histogram.items())},'eligible_triples':eligible}

def melnikov():
    # At h=1/6 use u=sqrt(2x+1), 0<=u<=sqrt(3); all square roots cancel.
    i0=F(3)-F(9,5)
    i1=(F(36,5)-F(27,7)-F(3))/2
    pairs=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(-1,10),F(1)),(F(-1,5),F(1))]
    assert i0==F(6,5) and i1==F(6,35)
    return {'separatrix_I0':str(i0),'separatrix_I1':str(i1),'ratio_limit':str(i1/i0),
            'pairs':[{'a':str(a),'b':str(b),'M_separatrix_limit':str(a*i0+b*i1)} for a,b in pairs],
            'interior_zero_pair':['-1/10','1'],
            'reason':'I1/I0 tends to 0 at the center and to 1/7 at the separatrix; continuity crosses 1/10. Simplicity is not established.'}

if __name__=='__main__':
    result={'86':{mode:oracle(mode) for mode in ('baseline','parity','redundant')}}
    for row in result['86'].values():
        checks=[oracle_verify(row['strategy'],x) for x in range(7)]
        assert sum(checks)==row['successful_secrets'];row['direct_strategy_successes']=checks
    result['93']=strassen_screen();result['100']=melnikov()
    (OUT/'computation_priority_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
