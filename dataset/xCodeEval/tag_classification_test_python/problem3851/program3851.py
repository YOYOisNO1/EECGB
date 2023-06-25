    import math,sys,bisect,heapq
    from collections import defaultdict,Counter,deque
    from itertools import groupby,accumulate
    #sys.setrecursionlimit(200000000)
    input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
    ilele = lambda: map(int,input().split())
    alele = lambda: list(map(int, input().split()))
    from functools import lru_cache
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
    #MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])
        
    N = int(input())
    A = alele()
    dp = {}
def fun(N,day,prev = -1):
        if day >= N:
            return 0
        if dp.get((day,prev),-1) != -1:
            return dp[(day,prev)]
        if prev == -1:
            x = A[day]
            if x == 0:
                dp[(day,prev)] =  1 + fun(N,day+1,-1)
                return dp[(day,prev)]
            elif x == 1:
                dp[(day,prev)] = min(1 + fun(N,day+1,-1), fun(N,day+1,2))
                return dp[(day,prev)]
            elif x == 2:
                dp[(day,prev)] = min(1 + fun(N,day+1,-1),fun(N,day+1,3))
                return dp[(day,prev)]
            elif x == 3:
                dp[(day,prev)] = min(1 + fun(N,day+1,-1),fun(N,day+1,2),fun(N,day+1,3))
                return dp[(day,prev)]
        elif prev == 2:
            x = A[day]
            if x == 0:
                dp[(day,prev)] = 1 + fun(N,day+1,-1)
                return dp[(day,prev)]
            elif x == 1:
                dp[(day,prev)] = 1 + fun(N,day+1,-1)
                return dp[(day,prev)]
            elif x == 2:
                dp[(day,prev)] = min(1 + fun(N,day+1,-1),fun(N,day+1,3))
                return dp[(day,prev)]
            elif x == 3:
                dp[(day,prev)] = min(1 + fun(N,day+1,-1),fun(N,day+1,3))
                return dp[(day,prev)]
        elif prev == 3:
            x = A[day]
            if x == 0:
                dp[(day,prev)] = 1 + fun(N,day+1,-1)
                return dp[(day,prev)]
            elif x == 1:
                dp[(day,prev)] = min(1 + fun(N,day+1,-1), fun(N,day+1,2))
                return dp[(day,prev)]
            elif x == 2:
                dp[(day,prev)] =1 + fun(N,day+1,-1)
                return dp[(day,prev)]
            elif x == 3:
                dp[(day,prev)] = min(1 + fun(N,day+1,-1),fun(N,day+1,2))
                return dp[(day,prev)]
            
    
    print(fun(N,0))
                
            
        
            