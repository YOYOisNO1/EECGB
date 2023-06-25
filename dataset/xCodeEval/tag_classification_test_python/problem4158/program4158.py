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
    
def main():
        h,m,s,t1,t2 = LI()
        h *= 5
        h %= 60
        h += 0.1
        m += 0.1
        s += 0.1
        a = sorted([h,m,s])
        a = [a[-1]-60] + a
        a.append(a[1] + 60)
        for i in range(4):
            if (a[i]/5.0 < t1 < a[i+1]/5.0 or a[i]/5.0 < t1+12 < a[i+1]/5.0) and (a[i]/5.0 < t2 < a[i+1]/5.0 or a[i]/5.0 < t2+12 < a[i+1]/5.0):
                return 'YES'
    
        return 'NO'
    
    
    print(main())
    
    