    d = dict()
    ans = 1e8
    
def solve(x,n):
    	global ans
    	if x in d:
    		return d[x]
    	ans = min(ans,n)
    	d[x] = n+1
    	for i in range(n-1):
    		if abs(ord(x[i])-ord(x[i+1])) == 1:
    			if x[i] > x[i+1]:
    				d[x] = min(d[x],solve(x[:i]+x[i+1:],n-1))
    			else:
    				d[x] = min(d[x],solve(x[:i+1]+x[i+2:],n-1))
    	else:
    		d[x] = n
    	return d[x]
    
    n = int(input())
    s = input()
    solve(s,n)
    print(n-ans)