def program4225():
    r,c,n,m = map(int, input().strip().split())
    x = []
    for i in xrange(r):
    	x.append([0]*c)
    for i in xrange(n):
    	a,b = map(int, input().strip().split())
    	x[a-1][b-1] = 1
    count = 0
    for i in range(r):
    	for j in range(c):
    		#i,j is the starting point
    		# generate all the rectangles possible and find sum and if greater than k, add 1.
    		addition = 0
    		for k in range(i,r):
    			for l in range(j,c):
    				addition += x[k][l]
    		if(addition >= m):
    			count += 1
    		addition = 0
    		for k in range(j,c):
    			for l in range(i,r):
    				addition += x[l][k]
    		if(addition >= m):
    			count += 1
    print count