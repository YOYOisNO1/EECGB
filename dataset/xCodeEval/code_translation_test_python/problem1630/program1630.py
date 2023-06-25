    
    class primes():
    def __init__(self, n):
            self.prime_num = n
            self.min_prime = [-1] * (self.prime_num + 1)  # 2以上の自然数に対して最小の素因数を表す
            self.min_prime[0] = 0
            self.min_prime[1] = 1
            i = 2
            self.prime = []
            self.memo_prifac = {}
            while i <= self.prime_num:
                if self.min_prime[i] == -1:
                    self.min_prime[i] = i
                    self.prime.append(i)
                for j in self.prime:
                    if i * j > self.prime_num or j > self.min_prime[i]: break
                    self.min_prime[j * i] = j
                i += 1
    
    def prifac(self, n):
            # 素因数分解した結果を返す
            if n in self.memo_prifac:
                return self.memo_prifac[n]
            res = {}
            x = n
            while x > 1:
                p = self.min_prime[x]
                if p in res:
                    res[p] += 1
                else:
                    res[p] = 1
                x //= p
    
            # self.memo_prifac[n] = res  #場合によってはこの行を消すと高速化
    
            return res
    
    def divisors(self, n):
            # 約数列挙 メモした方がいいかも
            if n== 1: return [1]
            prf = self.prifac(n)
            keys = [key for key in prf]
    
        def divsearch(i):
                if i == len(keys) - 1:
                    return [keys[i] ** j for j in range(prf[keys[i]] + 1)]
                else:
                    res = []
                    subres = divsearch(i + 1)
                    p = keys[i]
                    for j in range(prf[p] + 1):
                        for node in subres:
                            res.append(node * p ** j)
                    return res
    
            return divsearch(0)
    
    
    from math import gcd
def lcm(a,b):
        return a*b//gcd(a,b)
    mod=10**9+7
    n=int(input())
    ans=0
    pri=primes(n+3)
    dp=[0]*(n+3)
    for c in range(1,n-1):
        k=n-c
        yaku=pri.divisors(k)
        yaku.sort(reverse=True)
        for g in yaku:
            m=k//g
            dp[g]=m-1
            for j in yaku:
                if j>g and j%g==0:dp[g]-=dp[j]
            ans+=(c*g//gcd(g,c))*dp[g]
            ans%=mod
        for g in yaku:dp[g]=0
    print(ans)
    
    
    