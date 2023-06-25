def program4026():
    from itertools import permutations as p
    r=map(int,input().split())
    print len([ x for x in range(r[4],r[5]+1) if sum([ x == eval('%'.join(map(str, [x]+list(e)))) for e in p(r[:4])])>6])