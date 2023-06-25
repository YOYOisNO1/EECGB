    import sys,os,io
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
        max_n = min(max_n, mod - 1)
    
        fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
        fact[0] = 1
        for i in range(max_n):
            fact[i + 1] = fact[i] * (i + 1) % mod
    
        inv_fact[-1] = pow(fact[-1], mod - 2, mod)
        for i in reversed(range(max_n)):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    def nCr_mod(n, r):
            res = 1
            while n or r:
                a, b = n % mod, r % mod
                if a < b:
                    return 0
                res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
                n //= mod
                r //= mod
            return res
    
        return nCr_mod
    
    ncr = make_nCr_mod()
    mod = 10**9 + 7
    n,k = [int(i) for i in input().split()]
    dp = [1]
    for i in range (1,n+1):
        dp.append(ncr(n,i))
    for i in range (1,len(dp)):
        dp[i]+=dp[i-1]
        dp[i]%=mod
    print(dp[min(n,k)])