    #from __future__ import division
    import itertools
    from fractions import gcd
    from math import sqrt
    from bisect import bisect_left , bisect_right
    import heapq
    from collections import deque , defaultdict , Counter
    from itertools import combinations as C
def Ls():
    	return list(input())
def get(a):
    	return map(a , input().split())
def Int():
    	return int(input())
def Str():
    	return input()
    
    a = get(int)
    b = get(int)
    c = get(int)
    d = get(int)
    
    a1 = [b[0],c[1],d[2]]
    b1 = [c[0],d[1],a[2]]
    c1 = [d[0],a[1],b[2]]
    d1 = [a[0],b[1],c[2]]
    
    if a[-1] == 1:
    	if 1 in a1:
    		print 'YES'
    		exit(0)
    if b[-1] == 1:
    	if 1 in b1:
    		print 'YES'
    		exit(0)
    if c[-1] == 1:
    	if 1 in c1:
    		print 'YES'
    		exit(0)
    if d[-1] == 1:
    	if 1 in d1:
    		print 'YES'
    		exit(0)
    
    print 'NO'
    
    
    
    
    	
    