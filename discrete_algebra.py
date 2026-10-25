import itertools as it, json, pathlib
OUT=pathlib.Path(__file__).parent

def corr(s,t): return sum(s[j]*s[(j+t)%len(s)] for j in range(len(s)))
def complementary(q): return all(sum(corr(s,t) for s in q)==0 for t in range(1,len(q[0])))
seq=[(1,)+p for p in it.product((-1,1),repeat=2)]
valid=[]; all_parent_append_pairs=0; invalid_parent_with_extension=0
for q in it.product(seq,repeat=4):
    parent_valid=complementary(q)
    extensions=[]
    for signs in it.product((-1,1),repeat=8):
        all_parent_append_pairs+=1
        ext=tuple(q[i]+signs[2*i:2*i+2] for i in range(4))
        if complementary(ext): extensions.append(ext)
    if parent_valid:valid.append({'parent':q,'extension_count':len(extensions),'first_extension':extensions[0] if extensions else None})
    elif extensions:invalid_parent_with_extension+=1
r49={'normalized_parents_tested':256,'valid_parents':len(valid),'append_choices_per_parent':256,'total_parent_append_pairs_tested':all_parent_append_pairs,'append_pairs_with_valid_parent':len(valid)*256,'invalid_parents_with_complementary_extensions':invalid_parent_with_extension,'parents_without_extension':sum(not x['extension_count'] for x in valid),'extension_count_distribution':{str(c):sum(x['extension_count']==c for x in valid) for c in sorted({x['extension_count'] for x in valid})},'parents':valid}

# Classify equality cases from the former four-element pilot, rather than
# treating the already known count as the new result.
eq=[]
for fam_bits in range(1,1<<16):
    F=[s for s in range(16) if fam_bits>>s&1]
    if not any(F): continue
    if any(not (fam_bits>>(a|b)&1) for a in F for b in F): continue
    freq=[sum(bool(s>>i&1) for s in F) for i in range(4)]
    if 2*max(freq)!=len(F): continue
    blocks=[s for s in F if s and not any(t and t!=s and t&s==t for t in F)]
    disjoint=all(not (a&b) for a,b in it.combinations(blocks,2))
    generated={0}
    for b in blocks: generated|={s|b for s in list(generated)}
    eq.append({'family':F,'minimal_blocks':blocks,'disjoint':disjoint,'all_block_unions':generated==set(F),'block_sizes':sorted(b.bit_count() for b in blocks)})
r37={'equality_families_classified':len(eq),'all_disjoint_block_union_families':all(x['disjoint'] and x['all_block_unions'] for x in eq),'isomorphism_types_by_block_sizes':sorted({tuple(x['block_sizes']) for x in eq}),'families':eq}

triples=list(it.combinations(range(5),3)); foursets=list(it.combinations(range(5),4))
tetramasks=[sum(1<<triples.index(t) for t in it.combinations(S,3)) for S in foursets]
perms=list(it.permutations(range(5)))
maps=[[triples.index(tuple(sorted(p[i] for i in t))) for t in triples] for p in perms]
def canon(m):
    return min(sum(1<<mp[j] for j in range(10) if m>>j&1) for mp in maps)
ok=[]
for m in range(1<<10):
    if all(m&t!=t for t in tetramasks): ok.append(m)
types={canon(m) for m in ok}; ex=max(m.bit_count() for m in ok)
def cyclic_construction(n):
    A=[i%3 for i in range(n)]; E=[]
    for t in it.combinations(range(n),3):
        counts=[sum(A[v]==c for v in t) for c in range(3)]
        if counts==[1,1,1] or any(counts[i]==2 and counts[(i+1)%3]==1 for i in range(3)): E.append(t)
    eset=set(E)
    assert all(not all(t in eset for t in it.combinations(S,3)) for S in it.combinations(range(n),4))
    return len(E)
r50={'labeled_systems_tested':1024,'tetrahedron_free_labeled':len(ok),'isomorphism_types':len(types),'edge_count_distribution':{str(e):sum(m.bit_count()==e for m in ok) for e in range(11)},'maximum_edges':ex,'extremal_type_count':sum(m.bit_count()==ex for m in types),'one_extremal_edge_set':[triples[j] for j in range(10) if next(m for m in ok if m.bit_count()==ex)>>j&1],'cyclic_construction_edge_counts':{str(n):cyclic_construction(n) for n in [9,12]}}
res={'37':r37,'49':r49,'50':r50}
(OUT/'discrete_algebra_results.json').write_text(json.dumps(res,indent=2)+'\n')
for k,r in res.items(): print(k,{a:b for a,b in r.items() if a not in ['parents','families']})
