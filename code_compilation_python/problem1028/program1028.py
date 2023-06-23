def program1028():
    x,y = map(int,input().split())
    if x==0 or y==0:
    	print "black"
    else:
    	r2 = x*x+y*y
    	for i in range(1001):
    		if i*i==r2:
    			print "black"
    			break
    		if i*i>r2:
    			print ["white","black"][(i+(x>0)+(y>0))%2]
    			break 