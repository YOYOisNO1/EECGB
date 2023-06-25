    import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
    
    sys.setrecursionlimit(10**7)
    inf = 10**20
    eps = 1.0 / 10**10
    mod = 998244353
    dd = [(-1,0),(0,1),(1,0),(0,-1)]
    ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)
    
def divisions(n):
        sq = int(math.sqrt(n)+1)
        d = collections.defaultdict(int)
        while n % 2 == 0:
            n //= 2
            d[2] += 1
        i = 3
        while n > 1 and sq >= i:
            if n % i == 0:
                n //= i
                d[i] += 1
            else:
                i += 2
    
        if n > 1:
            d[n] += 1
    
        r = [1]
        for k, v in d.items():
            for c in r[:]:
                for i in range(1,v+1):
                    r.append(c*(k**i))
    
        return sorted(r)
    
def main():
        n,k = LI()
    
        d = sorted(divisions(n))
        if len(d) < k:
            return -1
    
        return d[k-1]
    
    
    print(main())
    