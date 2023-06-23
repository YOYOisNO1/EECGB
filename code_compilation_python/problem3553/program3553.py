def program3553():
    st = input()
    
    l = [(-2,0),(-1,-2), (1,-2),(2,0),(1,2),(-1,2)]
    a = 6
    
    n = 1  
    ru = 0 
    yy = 0 
    while (ru <= st):
    	ru += n*a 
    	n += 1
    	yy += 1
    ru -= (n-1)*a
    yy -= 1 
    #print ru , yy 
    diff = st - ru 
    
    if (st <= 6):
    	if (st == 0):
    		print "0 0"
    		exit()
    
    	if (st == 1):
    		print "1 2"
    		exit()
    	if (st == 2):
    		print "-1 2"
    		exit()
    	if (st == 3):
    		print "-2 0"
    		exit()
    	if (st == 4):
    		print "-1 -2"
    		exit()
    	if (st == 5):
    		print "1 -2"
    		exit()
    	if (st == 6):
    		print "2 0"
    		exit()
     
    x = 2*(yy) 
    y = 0
    
    if (diff == 0):
    	print x , y 
    	exit()
    elif (diff == 1):	
    	x += 1
    	y += 2 
    	print x, y
    	exit()
    elif (diff <= yy+1):
    	x += 1 
    	y += 2
    	diff -= 1
    	x -= 1*diff
    	y += 2*diff
    	print x , y
    	exit()
    
    elif (diff > yy+1):
    	x += 1
    	y += 2 
    	x -= yy 
    	y += 2*yy 
    	diff -= yy+1
    	li = 0  
    
    	while (diff > yy+1 ) : 
    		if (li < len(l)):
    			x += l[li][0]*(yy+1)
    			y += l[li][1]*(yy+1)
    			diff -= (yy+1)
    			li += 1
    		else:
    			break 
    
    	x += l[li][0]*diff
    	y += l[li][1]*diff 
    	print x,y 
    	exit()