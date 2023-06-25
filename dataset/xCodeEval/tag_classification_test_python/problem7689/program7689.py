    mod = int(1e9+7)
    
    
def ksm(a: int, k: int) -> int:
        res = 1
        while k:
            if k & 1:
                res = (res * a) % mod
            a = (a*a) % mod
            k >>= 1
        return res
    
    
    m = int(input())
    dp = [0 for i in range(m + 1)]
    dp[1] = 0
    ans = 0
    inv = ksm(m, mod - 2)
    for i in range(2, m+1):
        fac = []
        j = 1
        while j*j <= i:
            if i % j == 0:
                fac.append(j)
                if(j != i//j):
                    fac.append(i//j)
            j += 1
        fac.sort()
        a = [0 for j in range(len(fac))]
        a[-1] = m // fac[-1]
        for j in range(len(fac) - 2, -1, -1):
            a[j] = m // fac[j]
            for k in range(j+1, len(fac)):
                if fac[k] % fac[j] == 0:
                    a[j] -= a[k]
            dp[i] += ((dp[fac[j]] + 1) * a[j] * inv) % mod
        dp[i] += a[-1] * inv % mod
        dp[i] = (dp[i] * m * ksm(m - a[-1], mod - 2)) % mod
        ans = (ans + dp[i] * inv) % mod
    
    print((ans + 1) % mod)