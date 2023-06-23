    import operator as op
def ncr(n, r):
        r = min(r, n-r)
        if r == 0: return 1
        numer = reduce(op.mul, xrange(n, n-r, -1))
        denom = reduce(op.mul, xrange(1, r+1))
        return numer//denom
    
    N,M,G = map(int, input().split())
def q(n):
    	return ncr(n+M, M)
    	
def f(n):
    	n -= 1
    	sign = 1
    	res = 0
    	while n >= 0:
    		res += sign * q(n)
    		sign *= -1
    		n -= 1
    	if M == 1:
    		res += sign
    	return res
    if M == 0:
    	print int(G == (N+1)%2)
    	raise SystemExit
    	
    		
    if G == 1:
    	print f(N)
    else:
    	print q(N)-f(N)