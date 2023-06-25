    from collections import deque
def readarray(foo): return [foo(x) for x in input().split()]
    
    
    stairs = []
    to = []
    color = []
    totalcolors = 0
    deg = []
    priority = []
    
    
def doit():
    	usedstairs = set()
    	visited = set([0])
    	stack = []
    
    	res = []
    	layer = [0]
    	
    	nextcolor = 1
    	hasnextcolor = totalcolors > 1
    
    	stack.append([0, -1, -1, 0])
    
    	while stack:
    		(u, source, parent, start) = state = stack[-1]
    
    		nexti = None
    		nexts = None
    		nextv = None
    		for i in xrange(start, len(to[u])):
    			s = to[u][i]
    			if s == source: continue
    			if s in usedstairs: continue
    			(v1, v2) = stairs[s]
    			v = v1 if v2 == u else v2
    			if not hasnextcolor and v in visited: continue
    			nexti = i
    			nexts = s
    			nextv = v
    			break
    
    		if nexti is None:
    			if parent != -1:
    				layer.append(parent)
    			stack.pop()
    			continue
    
    		if nextv not in visited:
    			visited.add(nextv)
    			layer.append(nextv)
    			state[3] = nexti
    			stack.append([nextv, nexts, u, 0])
    			continue
    	
    		usedstairs.add(nexts)
    		nextv = priority[nextcolor]
    		nextcolor += 1
    		hasnextcolor = totalcolors > nextcolor
    
    		res.append(layer)
    		res.append([nexts, u, nextv])
    		layer = [nextv]
    		visited.add(nextv)
    		
    		state[3] = nexti + 1
    		stack.append([nextv, nexts, u, 0])
    
    	res.append(layer)
    	return res if not hasnextcolor else None
    
    
def colorize(s, c):
    	if color[s] != -1: return
    	global totalcolors
    	totalcolors += 1
    	color[s] = c
    	deg[c] += 1
    	q = deque()
    	q.append(s)
    	while q:
    		u = q.popleft()
    		for stair in to[u]:
    			(v1, v2) = stairs[stair]
    			v = v1 if v2 == u else v2
    			if color[v] != -1: continue
    			color[v] = c
    			deg[c] += 1
    			q.append(v)
    
def run():
    	global to, color, deg, priority
    	n, m = readarray(int)
    	to = [[] for i in xrange(n)]
    	color = [-1] * n
    	deg = [0] * n
    	for i in xrange(m):
    		u, v = sorted(readarray(lambda x: int(x) - 1))
    		stairs.append((u, v))
    		to[u].append(i)
    		to[v].append(i)
    	for i in xrange(n):
    		colorize(i, i)
    
    	deg[0] = 100500
    	priority = sorted(range(n), lambda x, y: deg[y] - deg[x])[:totalcolors]
    	res = doit()
    	if res is None:
    		print("NO")
    		return
    
    	print("YES")
    	print len(res) / 2
    	for i, line in enumerate(res):
    		if i % 2 == 0:
    			print len(line),
    		print " ".join(map(lambda x: str(x + 1), line))
    
    run()