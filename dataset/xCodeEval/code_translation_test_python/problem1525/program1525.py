def program1525():
    #!/usr/bin/env python3
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    from math import factorial
    
    n, m = [int(item) for item in input().split()]
    fac = [0] * (n + 1)
    fac[0] = 1; fac[1] = 1
    for i in range(2, n+1):
        fac[i] = fac[i-1] * i % m
    ans = 0
    for i in range(1, n+1):
        val = fac[n - i + 1] * (n - i + 1) * fac[i]
        ans += val
        ans %= m
    print(ans)