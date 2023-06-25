def program4044():
    a, b = list(map(int, input().split()))
    parent = {}
    
    import queue
    q = queue.Queue()
    q.put(a)
    visited = {}
    finans = False
    parent[a] = -1
    while(q.qsize() > 0):
    
    	s = q.qsize()
    	ans = False	
    	for i in range(s):
    		node = q.get()
    		visited[node] = True
    		if(node == b):
    			ans = True
    			break
    		elif(node > b):
    			break
    		l = 2*node
    		r = node*10 + 1
    		parent[l] = node
    		parent[r] = node
    		if(l not in visited and l <= b):
    			q.put(l)
    		if(r not in visited and r <= b):
    			q.put(r)
    
    
    	if(ans == True):
    		finans = True
    		break
    
    if(finans == False):
    	print('NO')
    else:
    	print('YES')
    	p = b
    	arr = []
    	while(parent[p] != -1):
    		arr.append(p)
    		p = parent[p]
    	arr.append(a)
    	print(len(arr))
    	for i in range(len(arr) - 1, -1, -1):
    		print(arr[i], end = ' ')
    	print()