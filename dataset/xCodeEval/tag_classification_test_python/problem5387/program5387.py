    import sys
    #import random
    from bisect import bisect_left as lb
    from collections import deque
    #sys.setrecursionlimit(10**8)
    from queue import PriorityQueue as pq
    #from math import *
    input_ = lambda: sys.stdin.readline().strip("\r\n")
    ii = lambda : int(input_())
    il = lambda : list(map(int, input_().split()))
    ilf = lambda : list(map(float, input_().split()))
    ip = lambda : input_()
    fi = lambda : float(input_())
    ap = lambda ab,bc,cd : ab[bc].append(cd)
    li = lambda : list(input_())
    pr = lambda x : print(x)
    prinT = lambda x : print(x)
    f = lambda : sys.stdout.flush()
    inv =lambda x:pow(x,mod-2,mod)
    mod = 10**9 + 7
    
    fac = [1]
    inv = [1]
    
    mx = 2*10**5 + 10
    
    for i in range (1,mx) :
        x = (fac[-1]*i)%mod
        fac.append(x)
        inv.append(pow(x,mod-2,mod))
    
def ncr (n,r) :
        return (((fac[n]*inv[r])%mod ) * inv[n-r])%mod
    
    #print(ncr(10,3))
    for _ in range (ii()) :
        n,k = il()
        t = 0
        for i in range (0,n,2) :
            t = (t + ncr(n,i))%mod
    
        if (n%2 == 1) :
            t = (t+1)%mod
            ans = pow(t,k,mod)
    
            print(ans)
    
        else :
            l = 0
            w = 1
    
            l = (pow(2,n,mod)-t+mod)%mod
            l = (l-w+mod)%mod
    
            ans = 0
            curr = 1
    
            for i in range (k-1,-1,-1) :
                temp = (curr * pow(pow(2,n,mod),i,mod))%mod
    
                ans = (ans + temp)%mod
                curr = (curr * t) % mod
    
            ans = (ans + curr)%mod
    
            print(ans)