    from collections import Counter, defaultdict, deque
    import bisect
    from sys import stdin, stdout
    from itertools import repeat, permutations
    import math
    import heapq
    
    
    MOD = int(1e9+7)
    
def inp(force_list=False):
        re = map(int, input().split())
        if len(re) == 1 and not force_list:
            return re[0]
        return re
    
def inpf(force_list=False):
        re = map(float, input().split())
        if len(re) == 1 and not force_list:
            return re[0]
        return re
    
def inst():
        return input().strip()
    
def gcd(x, y):
       while(y):
           x, y = y, x % y
       return x
    
def lcm(x, y):
        return x*y/(gcd(x,y))
    
def qmod(a, b, mod=MOD):
        res = 1
        while b:
            if b&1:
                res = (res*a)%mod
            b >>= 1
            a = (a*a)%mod
            # print(b)
        return res
    
def inv(a):
        return qmod(a, MOD-2)
    
def query(num):
        print(num)
        stdout.flush()
        return inp()
    
    fac = [1]
    for i in range(1, 210000):
        fac.append(fac[-1]*i%MOD)
    
def C(n, k):
        return fac[n] * inv((fac[k]*fac[n-k])%MOD)%MOD
    
def my_main():
        kase = inp()
        pans = []
        cur = []
        for _ in range(kase):
            n, k = inp()
            odd, ev = qmod(2, n-1), qmod(2, n-1)
    
            # for i in range(n):
            #     if i%2==0:
            #         ev += C(n, i)
            #         ev %= MOD
            #     else:
            #         odd += C(n, i)
            #         odd %= MOD
            if n%2==1:
                odd -=1
            else:
                ev -= 1
            # print(ev,) odd
            tt = 1
            ans = 0
            add = n%2 + ev
            att = qmod(2, n)
            pre = 1
            for i in range(k):
                left = k-i-1
                left = qmod(2, left)
                left = qmod(left, n)
                # pre = qmod(add, max(0, i-1))
                ans += (pre*left*odd)%MOD
                tt *= att
                tt %= MOD
                pre = (pre*add)%MOD
            print((tt-ans+MOD)%MOD)
    
        # print('\n').join(pans)
    
    my_main()