def program2444():
    a, b, c, d, e, f = map(int, input().split())
    
    if b*d*f > a*c*e or (a == 0 and d > 0) or (c == 0 and b*d > 0):
    		print 'Ron'
    	else:
    		print 'Hermione'	