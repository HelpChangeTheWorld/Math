"""Exact periodic-complementary quadruple extension / sign-repair audit.
Four ordered sign sequences, each with first sign +1; positions stay ordered.
Append two independent signs per row; repairs may flip any noninitial old sign.
Integer bit coding: bit0 = second sequence position. No symmetry quotient.
"""
import itertools, json, time
from pathlib import Path
from collections import defaultdict, Counter
import numpy as np
OUT=Path(__file__).resolve().parent
def sequences(n):
    codes=np.arange(1<<(n-1),dtype=np.uint32)
    rows=np.ones((len(codes),n),dtype=np.int16)
    for j in range(1,n):
        rows[:,j]=1-2*((codes>>(j-1))&1).astype(np.int16)
    corr=np.stack([(rows*np.roll(rows,-t,axis=1)).sum(axis=1) for t in range(1,(n+1)//2)],axis=1)
    return rows,corr
def buckets(n):
    rows,corr=sequences(n); m=len(rows); b=defaultdict(list)
    for a in range(m):
        for c in range(m):
            b[tuple(int(x) for x in corr[a]+corr[c])].append((a,c))
    return rows,corr,b
def valid_codes(n):
    rows,corr,b=buckets(n); bits=n-1; values=[]
    for sig,ab in b.items():
        cd=b.get(tuple(-x for x in sig),[])
        if not cd:continue
        left=np.array([a|(bb<<bits) for a,bb in ab],dtype=np.uint32)
        right=np.array([c|(d<<bits) for c,d in cd],dtype=np.uint32)
        for chunk in np.array_split(left,max(1,(len(left)*len(right)+999999)//1000000)):
            values.append((chunk[:,None]|(right[None,:]<<(2*bits))).reshape(-1))
    return np.sort(np.concatenate(values)) if values else np.array([],dtype=np.uint32)
def extendable(n):
    """Return all length-n prefixes with some length-(n+2) valid extension."""
    _,_,b=buckets(n+2); bits=n-1; mask=(1<<bits)-1
    good=np.zeros(1<<(4*bits),dtype=np.bool_)
    total=0
    for sig,ab in b.items():
        cd=b.get(tuple(-x for x in sig),[])
        if not cd:continue
        total+=len(ab)*len(cd)
        left=np.unique(np.array([(a&mask)|((bb&mask)<<bits) for a,bb in ab],dtype=np.uint32))
        right=np.unique(np.array([(c&mask)|((d&mask)<<bits) for c,d in cd],dtype=np.uint32))
        for chunk in np.array_split(left,max(1,(len(left)*len(right)+999999)//1000000)):
            good[(chunk[:,None]|(right[None,:]<<(2*bits))).reshape(-1)]=True
    return good,total
def decode(code,n):
    rows,_=sequences(n); bits=n-1; mask=(1<<bits)-1
    return [rows[(int(code)>>(bits*r))&mask].tolist() for r in range(4)]
def direct_verify(rows):
    n=len(rows[0])
    return [sum(row[j]*row[(j+t)%n] for row in rows for j in range(n)) for t in range(1,n)]
def find_extension(prefix,n):
    seqs=decode(prefix,n)
    for app in itertools.product((-1,1),repeat=8):
        rows=[seqs[r]+list(app[2*r:2*r+2]) for r in range(4)]
        if all(v==0 for v in direct_verify(rows)):return rows
    return None
def main():
    started=time.monotonic(); result={"model":__doc__,"results":[]}
    for n in (3,5,7):
        parents=valid_codes(n); good,total_extensions=extendable(n)
        remaining=parents.copy(); histogram={}; witness=None; hardest=[]
        reached=good.copy()
        for d in range(0,5):
            hit=reached[remaining]; histogram[str(d)]=int(hit.sum())
            if d>=3:
                hardest.extend({"code":int(c),"parent":decode(int(c),n),"minimum_flips":d} for c in remaining[hit])
            if d>=3 and hit.any() and witness is None:
                code=int(remaining[np.flatnonzero(hit)[0]])
                for inds in itertools.combinations(range(4*(n-1)),d):
                    repaired=code
                    for bit in inds:repaired^=1<<bit
                    if good[repaired]:
                        ext=find_extension(repaired,n)
                        assert ext is not None
                        witness={"parent_code":code,"parent":decode(code,n),"parent_correlations":direct_verify(decode(code,n)),
                            "minimum_flips":d,"zero_based_flipped_bit_positions":list(inds),"repaired_prefix":decode(repaired,n),
                            "extension":ext,"extension_correlations":direct_verify(ext)}
                        break
            remaining=remaining[~hit]
            if not len(remaining):break
            old=reached; reached=old.copy()
            for bit in range(4*(n-1)):
                stride=1<<bit
                view=old.reshape(-1,2*stride)
                newview=reached.reshape(-1,2*stride)
                newview[:,:stride]|=view[:,stride:]
                newview[:,stride:]|=view[:,:stride]
        rec={"parent_length":n,"target_length":n+2,"all_normalized_parents":1<<(4*(n-1)),
            "valid_parents":int(len(parents)),"valid_extended_quadruples":int(total_extensions),
            "extendable_prefixes_all":int(good.sum()),"min_repair_histogram_valid_parents":histogram,
            "unclassified_parents":int(len(remaining)),"witness":witness,"parents_requiring_at_least_three_flips":hardest}
        result["results"].append(rec)
        print(json.dumps(rec),flush=True)
        (OUT/"results.json").write_text(json.dumps(result,indent=2))
    result["seconds"]=time.monotonic()-started
    (OUT/"results.json").write_text(json.dumps(result,indent=2))
if __name__=="__main__":main()

