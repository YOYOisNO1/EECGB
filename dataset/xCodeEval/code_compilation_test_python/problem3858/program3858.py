    import sys
    
def p(a):
    	for x in a:
    		print "".join(x)
    	sys.exit(0)
    
    a = []
    n = 6
    for i in range(n):
    	a.append(list(input()))
    
    p4 = [(0, 3), (0, 4), (1, 3), (1, 4)]
    
    
    for x, y in p4:
    	if a[x][y] == '.':
    		a[x][y] = 'P'
    		p(a)
    
    p2 = [(2, 0), (2, 1), (3, 0), (3, 1), (5, 3), (5, 3), (4, 3), (4, 4), (2, 6), (2, 7), (3, 6), (3, 7)]
    
    for x, y in p2:
    	if a[x - 2][y] == '.':
    		a[x - 2][y] = 'P'
    		p(a)
    
    
    for x, y in p2:
    	if a[x][y] == '.':
    		a[x][y] = 'P'
    		p(a)
    
    
    p1 = [(4, 0), (4, 1), (5, 0), (5, 1), (4, 6), (4, 7), (5, 6), (5, 7)]
    
    for x, y in p1:
    	if a[x][y] == '.':
    		a[x][y] = 'P'
    		p(a)
    