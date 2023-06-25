def program2923():
    import sys
    input = sys.stdin.readline
    
    n, mod = map(int, input().split())
    pow2 = [1]
    for _ in range(n + 5):
        pow2.append(2 * pow2[-1])
    l = n + 5
    fact = [1] * (l + 1)
    for i in range(1, l + 1):
        fact[i] = i * fact[i - 1] % mod
    inv = [1] * (l + 1)
    inv[l] = pow(fact[l], mod - 2, mod)
    for i in range(l - 1, -1, -1):
        inv[i] = (i + 1) * inv[i + 1] % mod
    x = [0]
    for i in range(1, n + 3):
        x.append(inv[i] * pow2[i - 1] % mod)
    dp0 = [0] * (n + 2)
    dp0[0] = 1
    ans = 0
    c = n
    while True:
        dp = [0] * (n + 2)
        for i in range(n):
            if not dp0[i]:
                continue
            dp0i = dp0[i]
            for j in range(i + 2, n + 2):
                k = j - i - 1
                dp[j] += dp0i * x[k] % mod
                dp[j] %= mod
        if not dp[-1]:
            break
        ans += fact[c] * dp[-1] % mod
        ans %= mod
        dp0 = dp
        c -= 1
    print(ans)