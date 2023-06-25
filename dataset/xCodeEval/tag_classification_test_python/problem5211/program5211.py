    #####################################   
    import atexit, io, sys , collections, heapq
    buffer = io.BytesIO() 
    sys.stdout = buffer
    @atexit.register 
def write(): sys.__stdout__.write(buffer.getvalue())   
    ##################################### 
    mod = 998244353
    
    n = int(input())
    mem = [1] * (n+1)
def f(n):
    
    	if n == 1: return 1
    	if n == 0: return 1
    	if n <= 1:
    		return 1
    	u,v = 1,1
    	ans = 0
    	"""
    	f(0) = 1
    	f(1) = 1
    	f(2) = f(1)
    	f(3) = f(2) + f(0)
    	     = 2
    	f(4) = f(3) + f(1)
    	     = 2 + 1
    	     = 3
    	f(5) = f(4) + f(2) + f(0)
    	"""
    	qo = collections.deque([1])
    	so = 1
    	qe = collections.deque([1])
    	se = 1
    	for t in range(2, n + 1):
    		if t % 2:
    			so += se
    			so %= mod
    			qo.append(se)
    		else:
    			se += so
    			se %= mod
    			qe.append(so)
    	return se if n % 2 else so
    
def pow(a,n):
    	if n == 0:return 1
    	r = pow(a, n//2) % mod
    	return r * r * (a if n % 2 else 1) % mod
    
    
    a = f(n)
    b = pow(2,n)
    #print(a,b)
    print(a) * pow(b, mod-2) % mod