def fact(n):
    	res = 1
    	for i in range(1, n + 1):
    		res = res * i
    	return res
    
def C(n, k):
            #if k > n:
            #	return -1
    	res = fact(n)/(fact(k)*fact(n - k))
    	return int(res)
    
    	'''
    __inp = input().split(' ')
    N = int(__inp[0])
    M = int(__inp[1])
    T = int(__inp[2])
    
    res = 0
    for i in range(4, T):
    	res += C(N, i)*C(M, T - i)
    
    print int(res)
    '''
    for i in range(1, 31):
    	print('{', end='')
    	for j in range(1, 31):
    		print(C(i, j), sep='', end=', ')
    	print(C(i, i), '}, ', end='', sep='')
    
    	