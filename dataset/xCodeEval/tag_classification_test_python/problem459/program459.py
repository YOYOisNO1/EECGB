    # Template 1.0
    import sys, re, math
    from collections import deque, defaultdict, Counter, OrderedDict
    from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
    from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
        temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
        toret = {}
        for tup in temp:
            toret[tup[0]] = tup[1]
        return toret
def sortDictWithKey(passedDic):
        return dict(OrderedDict(sorted(passedDic.items())))
    sys.setrecursionlimit(10 ** 9)
    INF = float('inf')
    mod = 10 ** 9 + 7
    
    
def solveBF(a, b):
        while(True):
            if(a==0 or b==0):
                return a, b
            if(a>b):
                k = (a-b)//(2*b)
                if(k<0):
                    k = 0
                a = a-2*b*k
            elif(a<b):
                k = (b-a)//(2*a)
                if(k<0):
                    k = 0
                b = b-2*k*a
            
            if(a>=2*b):
                a = a-2*b
            else:
                if(b>=2*a):
                    b = b-2*a
                else:
                    return a, b
    a, b = MAP()
    
    
    
    # print(a, b, k, 993//14)
    A,B = solveBF(a, b)
    print(A, B)
    
    
    
    