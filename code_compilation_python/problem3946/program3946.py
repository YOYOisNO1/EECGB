    
    from collections import Counter,defaultdict,deque
    #from heapq import *
    #from itertools import *
    #from operator import itemgetter
    #from itertools import count, islice
    #from functools import reduce
    #alph = 'abcdefghijklmnopqrstuvwxyz'
    #n,x = [int(_) for _ in input().split()]
    #s = input().strip()
    #sarr = [x for x in input().strip().split()]
    #import math
    #from math import *
    #from heapq import *
    import sys
    input=sys.stdin.readline
    #sys.setrecursionlimit(2**30)
    
    #ons = ['no','yes']
def solve():
        #n = int(input())
        h,w = [int(_) for _ in input().split()]
        cake = []
        for i in range(h):
            cake.append(input().strip())
        curh = 0
        curw = 0
        ans = 0
        d = 0
        while True:
            ii = d+curw
            jj = curh
            while ii>=curw:
                if ii<w and jj<h and cake[jj][ii] == '*':
                    ans+=1
                    curw = ii
                    curh = jj
                    d = 0
                    break
                else:
                    if ii==w-1 and jj==h-1:
                        print(ans)
                        return
                    ii-=1
                    jj+=1
            d+=1
    
    
    tt = 1#int(input())
    for test in range(tt):
        solve()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #