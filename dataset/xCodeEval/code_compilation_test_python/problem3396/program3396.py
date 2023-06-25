def GCD(a, b):
    	while a != b:
    		if a > b:
    			a = a - b
    		else:
    			b = b - a
    	return a	
    
    a, b, x, y = map(int, input().split())
    gcd = GCD(x, y)
    x/=gcd
    y/=gcd
    c = a/x
    
    d = b/y
     
    if c < d:
    	r1 = x*c
    	r2 = y*c
    elif d <= c:
    	r1 = x*d
    	r2 = y*d
    if r1*y == r2*x:
    	print r1, r2
    else:
    	print 0, 0
    	