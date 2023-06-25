    N, L, R = map(int, input().split())
    
    if N == 0:
    	print(0)
    	exit(0)
    
    ans = [0, 0]
    ans[0] = (0, 1)
    ans[1] = (1, 1)
    
def solve(n):
    	if n < 2: 
    		ans[n] = (n, 1)
    		return (n, 1)
    	arr = solve(n/2)
    	ans.append((arr[0] * 2 + n % 2, arr[1] * 2 + 1)) 
    	return (arr[0] * 2 + n % 2, arr[1] * 2 + 1)
    
    solve(N)
    
def func(k):
    	n = len(ans) - 1
    	m = N
    	total = 0
    	while n >= 0:
    		if k == ans[n][1]: 
    			total += ans[n][0] 
    			break
    		elif k > ans[n][1]/2:
    			total += ans[n-1][0] + (m%2)
    			k = ans[n][1]/2 - (ans[n][1] - k)
    			m /= 2
    			n -= 1
    		else:
    			m /= 2
    			n -= 1
    	return total
    
    print(ans[-1][0]) - func(L - 1) - func(ans[-1][1] - R)
    
    
    
    
    
    
    