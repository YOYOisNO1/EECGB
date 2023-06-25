    n,m = map(int,input().split())
    
    rows = input()
    columns = input()
    
def DFS(rows,columns,n,m):
    
    	ans = set()
    	for i in range(1,n+1):
    		for j in range(1,m+1):
    
    			stack = [(i,j)]
    			visited = set()
    
    			while len(stack):
    
    				
    				tempx,tempy = stack.pop()
    				
    				visited.add((tempx,tempy))
    
    				if (tempx,tempy) in ans:
    					ans.add((i,j))
    					break
    				if tempx < n and columns[tempy-1] == "^" and (tempx+1,tempy) not in visited:
    					stack.append((tempx+1,tempy))
    				elif tempx-1 >= 1 and columns[tempy-1] == "v" and (tempx-1,tempy) not in visited:
    					stack.append((tempx-1,tempy))
    				if tempy < m and rows[tempx-1] == "<" and (tempx,tempy+1) not in visited:
    					stack.append((tempx,tempy+1))
    				elif tempy-1 >= 1 and rows[tempx-1] == ">" and (tempx,tempy-1) not in visited:
    					stack.append((tempx,tempy-1))
    
    
    			if len(visited)==n*m:
    				ans.add((i,j))
    	
    	if len(ans) == n*m:
    		print("YES")
    
    	else:
    		print("NO")
    
    
    
    DFS(rows,columns,n,m)