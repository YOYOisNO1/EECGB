    from sys import stdin
    input=lambda :stdin.readline()[:-1]
    
    mod=998244353
    M=(10**5)*3+1 
    fac=[1]*M
    ninv=[1]*M
    finv=[1]*M
    for i in range(2,M):
      fac[i]=fac[i-1]*i%mod
      ninv[i]=(-(mod//i)*ninv[mod%i])%mod
      finv[i]=finv[i-1]*ninv[i]%mod
    
def binom(n,k):
      if n<0 or k<0:
        return 0
      if k>n:
        return 0
      return (fac[n]*finv[k]%mod)*finv[n-k]%mod
    
    n,k=map(int,input().split())
    dp=[0]*n
    dp[0]=1
    
    for i in range(1,k+1):
      ndp=[0]*n
      pows=[1]
      for j in range(n*n):
        pows.append(pows[-1]*(k-i+1)%mod)
      for j1 in range(n):
        for j2 in range(j1,n):
          c=j2*(j2-1)//2-j1*(j1-1)//2
          ndp[j2]+=binom(n-1-j1,j2-j1)*pows[c]%mod*dp[j1]
          ndp[j2]%=mod
      dp=ndp
    
    print(dp[-1])