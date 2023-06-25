    mod = 998244353
    
    f = [1]
    for i in range(1, 5010):
        f += [f[i - 1] * i % mod]
    
    
def powmod(n, k):
        if k == 0:
            return 1
        res = powmod(n, k // 2)
        res *= res
        res %= mod
        if k % 2:
            res *= n
            res %= mod
        return res
    
    
def inv(n):
        return powmod(n, mod - 2)
    
    
def c(n, k):
        return f[n] * inv(f[n - k]) % mod * inv(f[k]) % mod
    
    
def match(a, b):
        res = 0
        for i in range(min(a, b) + 1):
            res += c(a, i) * c(b, i) * f[i] % mod
            res %= mod
        return res
    
    
    n,m,k = list(map(int, input().split()))
    print(match(n, m) * match(n, k) * match(m, k) % mod)