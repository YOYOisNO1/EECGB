    from collections import Counter, OrderedDict
    from itertools import permutations as perm
    from collections import deque
    from sys import stdin
    from bisect import *
    from heapq import *
    import math
    
    g   = lambda : stdin.readline().strip()
    gl  = lambda : g().split()
    gil = lambda : [int(var) for var in gl()]
    gfl = lambda : [float(var) for var in gl()]
    gcl = lambda : list(g())
    gbs = lambda : [int(var) for var in g()]
    mod = int(1e9)+7
    inf = float("inf")
    
    n, = gil()
    a = gil()
    b = gil()
    maxi = 0
    for i in range(3):
    	maxi += min(a[i], b[(i+1)%3])
    # r, s, p
    
def score(i, j):
    	return 1 if (i+1)%3 == j else 0 
    
    
    mini = inf
    
    
def fun(a, b, ans=0):
    	global mini
    	if a == b == [0, 0, 0]:
    		# print(ans)
    		mini = min(ans, mini)
    	else:
    		for i in range(3):
    			if a[i]:
    				for j in range(3):
    					if b[j]:
    						na, nb = a[:], b[:]
    						mul = min(a[i], b[j])
    						na[i] -= mul
    						nb[j] -= mul
    						fun(na, nb, ans+score(i, j)*mul)
    
    fun(a, b)
    print(mini, maxi)