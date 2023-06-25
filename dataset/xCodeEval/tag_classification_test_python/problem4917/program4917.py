    import sys
    from bisect import bisect_left
    
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    
def solve(a):
        res = [0]
        for x in a:
            res.extend([(x+y) % m for y in res])
    
        return sorted(set(res))
    
    
    pre, suf = solve(a[:n//2]), solve(a[n//2:])
    suf_n = len(suf)
    ans = 0
    
    for x in pre:
        i = bisect_left(suf, (m-x-1) % m) % suf_n
        ans = max(ans, (x+suf[i-1]) % m, (x+suf[i]) % m, (x + suf[(i+1) % suf_n]) % m)
    
    print(ans)