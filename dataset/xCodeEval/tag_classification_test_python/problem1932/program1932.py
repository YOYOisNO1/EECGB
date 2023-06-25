    import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
    
    sys.setrecursionlimit(10**7)
    inf = 10**20
    eps = 1.0 / 10**15
    mod = 10**9+7
    
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
    
    
def main():
        n = I()
        r = []
        for i in range(max(0,n-100), n+1):
            t = i
            for c in str(i):
                t += int(c)
            if t == n:
                r.append(i)
    
        if not r:
            return 0
    
        t = str(len(r)) + '\n'
    
        return t + '\n'.join(map(str,r))
    
    
    print(main())
    
    