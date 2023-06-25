    import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
    
    sys.setrecursionlimit(10**7)
    inf = 10**20
    eps = 1.0 / 10**10
    mod = 10**9+7
    dd = [(-1,0),(0,1),(1,0),(0,-1)]
    ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
    
    
def main():
        n,k,d = LI()
    
        fm = {}
    def f(n, df):
            key = (n,df)
            if key in fm:
                return fm[key]
            if (not df and n < d) or n < 0:
                fm[key] = 0
                return 0
            if n == 0:
                fm[key] = 1
                return 1
            r = 0
            for i in range(1,k+1):
                r += f(n-i, df or i >= d)
            fm[key] = r % mod
            return fm[key]
    
        r = f(n, False)
    
        return r % mod
    
    
    print(main())
    
    