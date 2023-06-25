    from math import *
    N, M = 510, 3 * 10 ** 5 + 10
    
    g = [[] for _ in range(M)] 
    n , m = map(int, input().split())
    mx = [[False] * N for _ in range(N + 1)] 
    
    for _ in range(m):
    	u, v = map(int, input().split())
    	mx[u][v] = mx[v][u] = True
    
    all_eq = True
    mark = [False] * N
    for i in range(1, n + 1):
    	for j in range(i + 1, n + 1):
    		if not mx[i][j]:
    			all_eq = False
    			mark[i] = True
    			g[i].append(j)
    			g[j].append(i)
    
    if all_eq:
    	print("YES")
    	print(n * 'a')
    	exit(0)
    ans = [-1] * N
    
def dfs(v, c):
    	ans[v] = c
    	res = False
    	for u in g[v]:
    		if ans[u] == -1:
    			res |= dfs(u, 2 - c)
    		elif ans[u] == ans[v]:
    			return False
    	return res
    
    for i in range(1, n + 1):
    	if mark[i] and ans[i] == -1 and dfs(i, 0):
    		print("NO")
    		exit(0)
    
    for i in range(1, n + 1):
    	if len(g[i]) == 0:
    		ans[i] = 1
    	if ans[i] == -1:
    		print("NO")
    		exit(0)
    for i in range(1, n + 1):
    	for j in range(i + 1, n + 1):
    		if mx[i][j] != (abs(ans[i] - ans[j]) != 2):
    			print("NO")
    			exit(0)
    
    print("YES")
    for i in range(1, n + 1):
    	print(chr(ans[i] + ord('a')), end = '')
    print()