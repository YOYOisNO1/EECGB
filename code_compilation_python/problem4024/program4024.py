def program4024():
    from itertools import permutations as p
    r=map(int,input().split())
    P=list(p(r[:4]))
    print len([ x for x in range(r[4],r[5]+1) if sum([ x == eval('%'.join(map(str, [x]+list(e)))) for e in P])>6])