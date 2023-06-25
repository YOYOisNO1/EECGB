    from sys import stdin
    input = stdin.readline
    II = lambda :int(input())
    MI = lambda :map(int,input().split())
    LI = lambda :list(map(int,input().split()))
    ANS = []
    #文字列出力はListでつくってから''.join(ANS),文字列結合は遅い
    mod = 998244353
    f = [1] * (250+1)
    for i in range(1,250+1):
        f[i] = i * f[i-1]
        f[i] %= mod
    finv = [pow(f[x],mod-2,mod) for x in range(250+1)]
    cmb = lambda r,c:(f[r] * finv[r-c] * finv[c]) % mod
def cnv(k,n):
        return N * k + n
    N,K= map(int,input().split()) 
    dp = [0] * (N * (K+1))
    dp[cnv(0,0)] = 1
    for k in range(1,K+1):
        for n in range(N):
            for cnt in range(n+1):
                e = (n * (n-1)) //2 - ((n-cnt) * (n-cnt-1) )//2
                dp[cnv(k,n)] += ((dp[cnv(k-1,n-cnt)] * cmb(N-1-(n-cnt),cnt))%mod * pow(K-k+1,e,mod)) % mod
                dp[cnv(k,n)] %= mod
    print(dp[cnv(K,N-1)])
    
    
                