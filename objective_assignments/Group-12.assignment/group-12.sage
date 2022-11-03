def table(H,reps):
    cos_dict = {r:[r*h for h in H] for r in reps}
    ans = []
    for r1 in reps[1:]:
        for r2 in reps[1:]:
            ans+=[k for k in cos_dict.keys() if r1*r2 in cos_dict[k]]
    return ans
def get_subgroup(n,gens):
    H = set([])

    for g in gens:
        for a in range(Mod(g,n).multiplicative_order()):
           H.add(g^a)
    for p1,p2 in [(a,b) for a in gens for b in gens if a!=b]:
        for a in range(1,Mod(p1,n).multiplicative_order()):
            for b in range(1,Mod(p2,n).multiplicative_order()):
                H.add(p1^a*p2^b)
    return H
def get_coset_reps(G,H):
    cosets = [H]
    for g in G:
        cosets.append({g*h for h in H})
    reps = list({min(c) for c in cosets})
    reps.sort()
    all_elts = [g*h for h in H for g in reps]
    assert len(all_elts) == len(G)
    return reps
n_list = []
o_list = []
gen_list = []
cos_reps_list = []
H_list = []
for n in range(20,60):
    Gadd = IntegerModRing(n)
    G = Gadd.unit_group()
    o = G.order()
    if o % 6 == 0 and o>6:
        n_list.append(n)
        o_list.append(o)
        H = [H for H in G.subgroups() if H.order()==o/6][0]
        gen_list.append([Gadd(m) for m in list(H.gens())])
        H = get_subgroup(n,[Gadd(m) for m in list(H.gens())])
        cos_reps = get_coset_reps([Gadd(m) for m in G],list(H))
        cos_reps_list.append(cos_reps)
        H_list.append(list(H))
        #print(cos_reps)
        #print(H)
        #for a in G:
        #    print([Gadd(a)*Gadd(h) for h in H])
#print(n_list)
#print(o_list)
#print(gen_list)
#print(cos_reps_list)
#print(H_list)
#print(table(H_list[0],cos_reps_list[0]))
for i in range(len(H_list)):
    print(table(H_list[i],cos_reps_list[i]),",")
