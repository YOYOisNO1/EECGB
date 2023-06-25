    n, k, d = map(int, input().split())
    M = 1000000007
    
def solve(n, k):
    	if k == 0:
    		return 0
    	ans = [0] * (n + 1)
    	for i in range(1, min(n + 1, k + 1)):
    		ans[i] = 1
    	for i in range(1, n + 1):
    		ans[i] = sum(ans[max(1, i-k):i+1]) % M
    	return ans[n]
    
    
    print((solve(n, k) - solve(n, d - 1)) % M)