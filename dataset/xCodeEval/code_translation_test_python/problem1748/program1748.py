    from bisect import bisect_right as br
    
    d_a = []
    d_b = []
    
def solve(a, b):
        global d_a, d_b
        
        n = a + b
        ans = (1 + n) << 1
    
        for i in xrange(1, int(n ** 0.5) + 1):
            if n % i == 0:
                idx_a = br(d_a, i)
                idx_b = br(d_b, i)
                x_a = d_a[idx_a - 1]
                x_b = d_b[idx_b - 1]
                if ((a // x_a <= n // i) or (b // x_b <= n // i)): ans = min(ans, (i + n // i) << 1)
    
        return ans
    
    a, b = map(int, input().strip().split())
    
    for i in xrange(1, int(a ** 0.5) + 1):
        if a % i == 0: d_a.append(i)
    for i in xrange(1, int(b ** 0.5) + 1):
        if b % i == 0: d_b.append(i)
    
    print(solve(a,) b)