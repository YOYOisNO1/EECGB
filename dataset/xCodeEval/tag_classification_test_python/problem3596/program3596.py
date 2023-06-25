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
        n,t = LI()
        s = [c for c in S()]
    
        for i in range(t):
            f = 1
            for j in range(n-1):
                if f:
                    if s[j] == 'B' and s[j+1] == 'G':
                        s[j],s[j+1] = s[j+1],s[j]
                        f = 0
                    else:
                        f = 1
                else:
                     f = 1
    
        return ''.join(s)
    
    
    print(main())