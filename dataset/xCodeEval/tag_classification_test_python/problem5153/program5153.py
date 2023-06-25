    F = map(int, input().split())
    
    N = F[0]
    L = F[1]
    R = F[2]
    if N == 0:
    	print(0)
    	exit(0)
    M = [0, 0];M[0] = (0, 1);M[1] = (1, 1)
def chutiyapa():
    	print('hello ')
    
    	return
    
def psum():
    	F = [0 for x in range(100)]
    
def S(n):
    	if n < 2: 
    		M[n] = (n, 1)
    		return (n, 1)
    	A = S(n/2); M.append((A[0]*2 + n%2, A[1]*2 + 1)) 
    	return (A[0]*2 + n%2, A[1]*2 + 1)
    
    
def update(key):
    	n = len(M) - 1
    	m = N
    	cost = 0
    	while n >= 0:
    		if key == M[n][1]: 
    			cost += M[n][0] 
    			break
    		elif key > M[n][1]/2:
    			cost += M[n-1][0] + (m%2)
    			key = M[n][1]/2 - (M[n][1] - key)
    		m/=2
    		n-=1
    
    	return cost
    S(N)
    
    print(M[-1][0]) - (update(L - 1) + update(M[-1][1] - R))
    
    
    
    
    
    
    