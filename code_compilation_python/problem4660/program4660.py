def rotate(a,d):
    	# 90 180 270
    	if d==0:
    		return a
    	ret = [[0 for x in range(n)] for y in range(n)] 
    
    	for i in range(n):
    		for j in range(n):
    			ret[n-1-j][i]=a[i][j]
    	d -= 90
    	return rotate(ret,d)
    
    
def flip(a,v):
    	ret = [[0 for x in range(n)] for y in range(n)] 
    	if v:
    		for i in range(n):
    			for j in range(n):
    				ret[n-i-1][j] = a[i][j]
    	else:
    		for i in range(n):
    			for j in range(n):
    				ret[i][n-j-1] = a[i][j]
    	return ret
    
    n=int(input())
    a=[]
    b=[]
    
    # print range(0,n)
    
    for i in range(0,n):
    	a.append(input())
    for i in range(0,n):
    	b.append(input())
    ay = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
    	for j in range(n):
    		ay[i][j] = a[i][j]
    a = ay
    
    
    by = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(n):
    	for j in range(n):
    		by[i][j] = b[i][j]
    b = by
    
    # print 'a=',a,'b=',b
    
    phase = [rotate(a,360),rotate(a,90),rotate(a,180),rotate(a,270)]
    p = []
    for item in phase:
    	p.append(item)
    	p.append(flip(item,1))
    	p.append(flip(item,0))
    
    if b in p:
    	print 'TRUE'
    else:
    	print 'NO'
    
    # print a[1][2]
    
    