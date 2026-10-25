"""Enumerate all variable orders by subset recurrence; exact integer truth tables."""
from pathlib import Path
import json,time
import numpy as np

ROOT=Path(__file__).parent

def enumerate_any(n):
    N=1<<n
    ALL=(1<<N)-1
    xmask=[sum(1<<x for x in range(N) if x>>j&1) for j in range(n)]
    classes={0:{0,ALL}}
    for k in range(1,n+1):
        t=time.time()
        for subset in range(1,1<<n):
            if subset.bit_count()!=k: continue
            fs=set()
            for j in range(n):
                if not(subset>>j&1): continue
                zero=ALL^xmask[j]; one=xmask[j]
                for f in classes[subset^(1<<j)]:
                    gs=(0,ALL,f,ALL^f)
                    low={a&zero for a in gs}
                    high={a&one for a in gs}
                    fs.update(a|b for a in low for b in high)
            classes[subset]=fs
        print('n',k,'count',len(classes[(1<<k)-1]),'seconds',time.time()-t,flush=True)
    return sorted(classes[(1<<n)-1])

if __name__=='__main__':
    fs=enumerate_any(6)
    tables=np.array(fs,dtype=np.uint64)
    np.save(ROOT/'allorders6_truth_tables.npy',tables)
    anf=tables.copy()
    for j in range(6):
        mask=sum(1<<m for m in range(64) if not(m>>j&1))
        anf^=(anf&np.uint64(mask))<<np.uint64(1<<j)
    higher_degree=sum(1<<m for m in range(64) if m.bit_count()>2)
    quad=(anf&np.uint64(higher_degree))==0
    pops=np.unpackbits(tables.view(np.uint8).reshape(-1,8),axis=1,bitorder='little').sum(axis=1)
    balanced=tables[quad&(pops==32)]
    np.save(ROOT/'balancedquadratic6_truth_tables.npy',balanced)
    print('saved',len(fs),flush=True)
