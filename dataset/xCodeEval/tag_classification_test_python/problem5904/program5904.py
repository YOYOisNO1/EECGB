    #from __future__ import division
    import itertools
    from fractions import gcd
    from math import sqrt
    from bisect import bisect_left
    import heapq
    
def Ls():
    	return list(input())
def get(a):
    	return map(a , input().split())
def Int():
    	return int(input())
def Str():
    	return input()
    
    #######################_|_#######################
    #JMD
def DFSvisit(G, v, visited, order, component):
        visited[v] = component
        for w in G[v]:
            if not visited[w]:
                DFSvisit(G, w, visited, order, component)
        order.append(v);
    
def DFS(G, sequence, visited, order):
        components = 0
        for v in sequence:
            if not visited[v]:
                components += 1
                DFSvisit(G, v, visited, order, components)
    n = input()
    n, m = n,n
    har = get(int)
    G = [[] for i in xrange(n)]
    Gt = [[] for i in xrange(n)]
    for i in xrange(m):
        a, b = i+1,har[i]
        G[a-1].append(b-1)
        Gt[b-1].append(a-1)
    
    order = []
    components = [0]*n
    from fractions import gcd
    
def lcm(a, b):
        """Return lowest common multiple."""
        return a * b // gcd(a, b)
    
    
    
    DFS(G, xrange(n), [0]*n, order)
    DFS(Gt, reversed(order), components, [])
    
    #print(max(components))
    #print(components)
    sc_c = dict()
    for i in xrange(n):
    	to = components[i]	
    	if to not in sc_c:
    		sc_c[to] = [i]
    	else:
    		sc_c[to].append(i)
    flag = True
    for i in sc_c:
    	if len(sc_c[i]) == 1:
    		at = sc_c[i][0]
    		if at + 1!= har[at]:
    			flag = False
    
    if flag:
    	#print("LCM")
    	st = []
    	for i in sc_c:
    		chk = len(sc_c[i])
    		if chk % 2 == 0:st.append(chk/2)
    		else:st.append(chk)
    	print(reduce(lcm,st))
    else:print(-1)
    		
    
    
    
    
    
    	
    
    
    
    
    	