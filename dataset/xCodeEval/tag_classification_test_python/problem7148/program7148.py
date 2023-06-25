    
    
    class combination():
    def __init__(self,N,p):#Nは上限,pはmod
            self.fact = [1,1]
            self.factinv = [1,1]
            self.inv = [0,1]
            for i in range(2, N + 1):
                self.fact.append((self.fact[-1] * i) % p)
                self.inv.append((-self.inv[p % i] * (p // i)) % p)
                self.factinv.append((self.factinv[-1] * self.inv[-1]) % p)
    def cmb(self,n, r,p):
            if (r < 0) or (n < r):
                return 0
            r = min(r, n - r)
            return self.fact[n] * self.factinv[r] * self.factinv[n-r] % p
def cmb2(x):
        return (x * (x-1))//2
    mod = 998244353
    C = combination(10**4,mod)
    N,K= map(int,input().split()) 
    dp = [[0] * (N) for _ in range(K+1)]
    dp[0][0] = 1
    for k in range(1,K+1):
        for n in range(N):
            for cnt in range(n+1):
                e = cmb2(n) - cmb2(n-cnt)
                dp[k][n] += dp[k-1][n-cnt] * C.cmb(N-1-(n-cnt),cnt,mod) * pow(K-k+1,e,mod)
                dp[k][n] %= mod
    print(dp[K][N-1])