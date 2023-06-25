def program292():
    import sys
    
    a = 0
    n = 0
    g = None
    c = 0
    
    for line in sys.stdin:
    	line = line[0:len(line)]
    	l = line.split(" ")
    	if a != 0:
    		c = int(l[0])
    		g = [int(l[i]) for i in range(1,n)]
    		
    	else:
    		n = int(l[0])
    		a = 1
    
    g.sort(reverse = True)
    b = 0
    while g[0] >= c:
    	b = b + 1
    	c = c + 1
    	g[0] = g[0]-1
    	t = g[0]
    	i = 1
    	while g[i] > t:
    		g[i-1] = g[i]
    		g[i] = t
    		i = i + 1
    
    print b