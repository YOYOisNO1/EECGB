    #
    # Yet I'm feeling like
    # 	There is no better place than right by your side
    # 		I had a little taste
    # 			And I'll only spoil the party anyway
    # 				'Cause all the girls are looking fine
    # 					But you're the only one on my mind
    
    
    import sys
    inf = float("inf")
    #sys.setrecursionlimit(1000000)
    
    
    # abc='abcdefghijklmnopqrstuvwxyz'
    # abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    mod,MOD=1000000007,998244353
    # vow=['a','e','i','o','u']
    # dx,dy=[-1,1,0,0],[0,0,1,-1]
    
    # from cmath import sqrt
    # from collections import deque, Counter, OrderedDict,defaultdict
    # from heapq import nsmallest, nlargest, heapify,heappop ,heappush, heapreplace
    # from math import ceil,floor,log,sqrt,factorial,pow,pi,gcd,log10,atan,tan
    # from bisect import bisect_left,bisect_right
    # import numpy as np
    
def is_subsq(a,b):   # is 'a' a subsequence of 'b'
        i=0;j=0       # i-->b and    j---->a
        while i<len(b) and j<len(a):
            if a[j]==b[i]:
                j+=1
            i+=1
        return j==len(a)
    
    
def get_array(): return list(map(int , sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()
    
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    l = [-1]
    r = [n]
    c = 0
    for i in range(n):
        if s[i] == t[c]:
            l.append(i)
            c += 1
            if c >= m:
                break
    c = 0
    for i in range(n):
        if s[-1-i] == t[-1-c]:
            r.append(n-1-i)
            c += 1
            if c >= m:
                break
    mx = 0
    # print(l)
    # print(r)
    for i in range(m+1):
        mx = max(mx, r[m-i]-l[i]-1)
    print(mx)