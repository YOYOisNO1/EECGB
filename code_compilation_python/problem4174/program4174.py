    import sys
    import heapq
    import bisect
    import math
    
    INF = 10**9+7
    OFFLINE = 0
    N = 101010
    sys.setrecursionlimit(INF)
    
def fi():
    	return int(sys.stdin.readline())
    
def fi2():
    	return map(int, sys.stdin.readline().split())
    
def fi3():
    	return sys.stdin.readline().rstrip()
    
def fo(*args):
    	for s in args:
    		sys.stdout.write(str(s)+" ")
    	sys.stdout.write("\n")
    
    ##
    if OFFLINE:
    	sys.stdin = open("fin.txt", "r")
    	sys.stdout = open("fout.txt", "w")
    ##
    
def root(x):
    
    	while parent[x] != x:
    		parent[x] = parent[parent[x]]
    		x = parent[x]
    
    	return x
    
def union(x, y):
    
    	px = root(x)
    	py = root(y)
    
    	if px == py:
    		return
    
    	parent[px] = py
    	size[py] += size[px]
    	roots.remove(px)
    	enemy[py] = enemy[py].union(enemy[px])
    
    
    ##main
    
    n = fi()
    
    parent = [i for i in range(n+1)]
    size = [1 for i in range(n+1)]
    roots = set([i+1 for i in range(n)])
    
    E = []
    enemy = [set() for i in range(n+1)] 
    
    k = fi()
    
    for i in range(k):
    	u, v = fi2()
    	union(u, v)
    
    
    m = fi()
    
    for i in range(m):
    	u, v = fi2()
    
    	if root(u) == root(v):
    		roots.remove(root(u))
    
    
    ans = 0
    
    for r in roots:
    	ans = max(ans, size[r])
    
    fo(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    