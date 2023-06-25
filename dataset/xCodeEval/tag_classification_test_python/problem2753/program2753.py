    from math import factorial
    
    f = factorial
    
    
def C(n, k):
        return f(n) // (f(k) * f(n - k))
    
    
    n, m, t = map(int, input().split())
    ans = 0
    for i in range(4, n + 1):
        if i <= n and 0 < t - i <= m:
            #print(i, t - i, C(n, i), C(m, t - i))
            ans += C(n, i) * C(m, t - i)
    print(ans)