def minrem(l, s, e, d):
        if l[e] - l[s] <= d: return 0
        else: return 1 + min(minrem(l, s+1, e, d), minrem(l, s, e-1, d))
    
    n, d = input().split()
    d = int(d)
    l = input().split()
    l = [int(i) for i in l]
    l = sorted(l)
    print minrem(l, 0, int(n)-1, d)