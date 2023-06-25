    import sys
    from functools import reduce
    ints = (int(x) for x in sys.stdin.read().split())
    
    mod = 998244353
    
def mod_pow(a, k):
        r = 1
        while k and r:
            if k%2: r = (r*a)%mod
            k, a = k>>1, (a*a)%mod
        return r
    
    
def main():
        mul = lambda a,b: (a*b)%mod
    def nCk(n, k):
            assert 0<=k<=n
            return mul(fact[n], mod_pow(mul(fact[k], fact[n-k]), mod-2))
    
        n, k = next(ints), next(ints)
        if 0 <= k < n:
            fact = [1]*(n+1)
            for i in range(1, n+1):
                fact[i] = mul(fact[i-1], i)
            m, ans = n-k, 0
            for i in range(m):
                sign = 1 if i%2==0 else -1
                ans += sign*mul(nCk(m, i), mod_pow(m-i, n))
                ans %= mod
            ans = mul(ans, nCk(n,k))
            ans = mul(ans, 1+(k>0))
        else:
            ans = 0
        print(ans)
        return
    
    main()