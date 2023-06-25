    import sys
    input = sys.stdin.readline
    
    t = int(input())
    mod = pow(10, 9) + 7
    pow2 = [1]
    for _ in range(200005):
        pow2.append(2 * pow2[-1] % mod)
    l = 200005
    fact = [1] * (l + 1)
    for i in range(1, l + 1):
        fact[i] = i * fact[i - 1] % mod
    inv = [1] * (l + 1)
    inv[l] = pow(fact[l], mod - 2, mod)
    for i in range(l - 1, -1, -1):
        inv[i] = (i + 1) * inv[i + 1] % mod
    
def comb(n, r):
        return fact[n] * inv[r] % mod * inv[n - r] % mod if n >= r >= 0 else 0
    
    for _ in range(t):
        n, k = map(int, input().split())
        p = pow2[n]
        powp = [1]
        for _ in range(k + 5):
            powp.append(p * powp[-1] % mod)
        if n % 2:
            c = 1
            for i in range(0, n, 2):
                c += comb(n, i)
                c %= mod
            ans = pow(c, k, mod)
        else:
            c = 0
            for i in range(0, n - 1, 2):
                c += comb(n, i)
                c %= mod
            ans = pow(c, k, mod)
            x = 1
            for i in range(k):
                ans += x * powp[k - i - 1] % mod
                ans %= mod
                x *= c
                x %= mod
        print(ans)