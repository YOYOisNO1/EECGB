    n,k,d = map(int,input().split())
    import sys
    sys.setrecursionlimit(10**5)
    mod = int(1e9+7)
    import functools
    @functools.lru_cache(None)
def rec(n,d):
        if n<0:return 0
        if n==0:
            return d==0
        res = 0
        for i in range(1,k+1):
            if i>=d:
                res+=rec(n-i,0)
            else:
                res+=rec(n-i,d)
            res%=mod
        return res%mod
    print(rec(n,d)%mod)