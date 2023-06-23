    from functools import lru_cache
    n,k = map(int,input().split())
    mod = 998244353
    rng = 500100
    fctr = [1]
    for i in range(1,rng):
      fctr.append(fctr[-1]*i%mod)
def finv(x):
      return pow(fctr[x],mod-2,mod)
def cmb(n,k):
      if n<0 or k<0:
        return 0
      else:
        return fctr[n]*finv(n-k)*finv(k)%mod
    if n < k:
      print(0)
      exit()
    @lru_cache
def stable(n,k,mn):
      if n < k*mn:
        return 0
      dvs = set()
      for i in range(1,int((n+0.5)**0.5)+1):
        if n%i == 0:
          dvs.add(i)
          dvs.add(n//i)
      ret = 0
      dvs = list(dvs)
      ndvs = 0
      for i in dvs:
        if i >= mn:
          ndvs += 1
        if n//i >= k and i >= mn:
          ret += cmb(n//i-1,k-1)
          ret %= mod
      return ret
    ans = 0
    for i in range(k):
      ans += stable(n-i,k,i+1)
      ans %= mod
    print(ans)