def program7146():
    import sys
    input = sys.stdin.readline
    
    l = 255
    mod = 998244353
    fact = [1] * (l + 1)
    for i in range(1, l + 1):
        fact[i] = i * fact[i - 1] % mod
    inv = [1] * (l + 1)
    inv[l] = pow(fact[l], mod - 2, mod)
    for i in range(l - 1, -1, -1):
        inv[i] = (i + 1) * inv[i + 1] % mod
    
    n, k = map(int, input().split())
    dp0 = [0] * n
    dp0[0] = 1
    for i in range(k):
        dp = [0] * n
        p = [1]
        for j in range(n * (n + 1) // 2):
            p.append((i + 1) * p[-1] % mod)
        for j in range(n):
            c = 0
            if not dp0[j]:
                continue
            dp0j = dp0[j]
            for l in range(j, n):
                dp[l] += p[c] * inv[l - j] % mod * dp0j % mod
                dp[l] %= mod
                c += n - l - 2
        dp0 = dp
    ans = dp0[-1] * fact[n - 1] % mod
    print(ans)