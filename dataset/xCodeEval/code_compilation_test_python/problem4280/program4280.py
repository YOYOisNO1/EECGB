    from collections import defaultdict
    
    
def solve(s1, s2):
        d = defaultdict(set)
        for t1, t2 in s1:
            d[t1].add(t2)
            d[t2].add(t1)
    
        ans = set()
        for t1, t2 in s2:
            if d[t1] - {t2} > 0 and d[t2] - {t1} == 0:
                ans.add(t1)
            elif d[t1] - {t2} == 0 and d[t2] - {t1} > 0:
                ans.add(t2)
            elif d[t1] - {t2} > 0 and d[t2] - {t1} > 0:
                return -1
    
        if len(ans) > 1:
            return 0
        if len(ans) == 1:
            return list(ans)[0]
    
    
    n, m = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    b = [int(x) for x in input().strip().split()]
    
    a = set(tuple(sorted([a[i*2], a[i*2+1]])) for i in range(n) if a[i*2] != a[i*2+1])
    b = set(tuple(sorted([b[i*2], b[i*2+1]])) for i in range(m) if b[i*2] != b[i*2+1])
    
    ans = min(solve(a, b), solve(b, a))
    print(ans)