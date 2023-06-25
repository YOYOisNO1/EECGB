    import collections
def g(s,k,u):
    	cc = collections.Counter(s)
    	p = cc[u] +	 min(k,len(s) - cc[u])
    	return p * (p-1)/2
    
    
def f(s,t,i,a,k):
    	ans = 0
    	if mem[i][k][a] != -1 : return mem[i][k][a]
    	if i == len(s): return 0
    	c = (1 if s[i] != t[0] else 0)
    	if k - c >= 0: ans = max(ans, f(s,t,i + 1, a + 1, k - c))
    	c = (1 if s[i] != t[1] else 0)
    	if k - c  >= 0: ans = max(ans, f(s,t,i + 1, a, k - c) + a)
    	ans = max(ans, f(s,t,i+1,a,k))
    	mem[i][k][a] = ans
    	return ans
    n,k = map(int, input().split())
    s,t = input(),input()
    
    mem = [[[-1 for uu in range(len(s)+1)] for jj in range(k+1)] for ii in range(len(s)+1)]
    print(f(s,t,0,0,k)) if t[0] != t[1] else g(s,k,t[0])