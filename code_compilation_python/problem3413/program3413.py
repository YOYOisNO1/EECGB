    d_a = []
    d_b = []
    
def solve(a, b):
        global d_a, d_b
        
        n = a + b
        ans = (1 + n) << 1
    
        for i in xrange(1, int(n ** 0.5) + 1):
            if n % i == 0:
                j = 0
                while j < len(d_a) and d_a[j] <= i:
                    if (a // d_a[j] <= n // i):
                        ans = min(ans, (i + n // i) << 1)
                    j += 1
    
        for i in xrange(1, int(n ** 0.5) + 1):
            if n % i == 0:
                j = 0
                while j < len(d_b) and d_b[j] <= i:
                    if (b // d_b[j] <= n // i):
                        ans = min(ans, (i + n // i) << 1)
                    j += 1
    
        return ans
    
    a, b = map(int, input().strip().split())
    
    for i in xrange(1, int(a ** 0.5) + 1):
        if a % i == 0: d_a.append(i)
    for i in xrange(1, int(b ** 0.5) + 1):
        if b % i == 0: d_b.append(i)
    
    print solve(a, b)