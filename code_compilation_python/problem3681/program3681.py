    #!/usr/bin/env python
    from __future__ import division, print_function
    
    import sys
    from atexit import register
    from io import BytesIO
    
    
    sys.stdin = BytesIO(sys.stdin.read())
    input = lambda: sys.stdin.readline().rstrip('\r\n')
    
    sys.stdout = BytesIO()
    register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
    
    
def solve(p, q):
        dp = [1]
        for i in range(q):
            dp.append(dp[-1] * p % 1000000007)
        for i in range(1, q + 1):
            dp[i] = (dp[i] + dp[i - 1]) % 1000000007
        for _ in range(k):
            dp1 = [1] * (q + 1)
            for i in range(1, q + 1):
                dp1[i] = (dp1[i - 1] + dp[i] * inv[i + 1]) % 1000000007
            dp = dp1
        return (dp[-1] - dp[-2]) % 1000000007
    
    
    inv = [pow(i, 1000000005, 1000000007) for i in range(60)]
    
    n, k = map(int, input().split())
    ans = 1
    
    if 4 <= n:
        c = 0
        while n % 2 == 0:
            c += 1
            n //= 2
        if c:
            ans = ans * solve(2, c) % 1000000007
    
    if 9 <= n:
        c = 0
        while n % 9 == 0:
            c += 1
            n //= 9
        if c:
            ans = ans * solve(2, c) % 1000000007
    
    i = 5
    while i * i <= n:
        c = 0
        while n % i == 0:
            c += 1
            n //= i
        if c:
            ans = ans * solve(i, c) % 1000000007
        i += 2 if i % 3 == 2 else 4
    
    if n > 1:
        ans = ans * solve(n, 1) % 1000000007
    
    print(ans)