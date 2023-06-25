    """
    MAXN = 10;
    dp = [[[-1 for i in xrange(2)] for j in xrange(2)] for k in xrange(MAXN + 1)]
    dp2 = [[-1 for i in xrange(2)] for j in xrange(MAXN + 1)];
    
def f(n,c1,c2):
    	if not n: return c2;
    	if dp[n][c1][c2] != -1: return dp[n][c1][c2];
    	#set to 0
    	dp[n][c1][c2] = f(n-1,0,c2);
    	#set to 1
    	dp[n][c1][c2] += f(n-1,1,c2 or c1);
    	return dp[n][c1][c2];
    
def g(n,c):
    	if not n: return 1;
    	if dp2[n][c] != -1: return dp2[n][c];
    	dp2[n][c] = g(n-1,0);
    	if not c: dp2[n][c] += g(n-1,1);
    	return dp2[n][c];
    
    """
    
    fib = {0:1,1:1};
def get_fib(n,m):
    	if n in fib: return fib[n]%m;
    	k = n >> 1;
    	if n%2 == 0: 
    		fib[n] = pow(get_fib(k,m),2,m) + pow(get_fib(k - 1,m),2,m);
    		if fib[n] >= m: fib[n] -= m;
    	else:
    		fib[n] = get_fib(k,m) * (get_fib(k - 1,m) + get_fib(k + 1,m));
    		fib[n] %= m;
    	return fib[n]%m;
    
    n,k,l,m = map(int,input().split());
    g = get_fib(n + 1,m);
    f = pow(2,n,m) - g;
    if f < 0: f += m;
    q = k & ~((1 << l) - 1);
    if q: 
    	print(0;)
    else:
    	ctr = 0;
    	while(k):
    		ctr += k & 1;
    		k >>= 1;
    	if ctr > l: print(0;)
    	else:
    		print((pow(f,ctr,m)) * pow(g,l - ctr,m))%m