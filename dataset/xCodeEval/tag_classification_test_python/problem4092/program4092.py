    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import heapq
    from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return map(int, data().split())
    #sys.setrecursionlimit(100000)
    
    mod=998244353
    
def fac(x):
        f=1
        for i in range(2,x+1):
            f=(f*i)%mod
        return f
    n,m=mdata()
    ans=(fac(m)*(n-2)*pow(2,n-3,mod))*pow(fac(n-1),mod-2,mod)*pow(fac(m-n+1),mod-2,mod)
    print(ans%mod)