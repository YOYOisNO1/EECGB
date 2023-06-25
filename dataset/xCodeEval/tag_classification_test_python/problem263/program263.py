def program263():
    n, c = map(int,input().split())
    x = map(int,input().split())
    
    res = 0
    for i in xrange(n - 1):
    	res = max(res, x[i] - (x[i + 1] + c))
    	
    print(res)