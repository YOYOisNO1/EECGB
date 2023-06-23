def solver():	
    	x,y,m = map(int , input().split())
    	if(x >= 0 and y >= 0):
    		if(x >= m or y >= m):
    			print "0"
    			return
    	if(x <= 0 and y <= 0):
    		if(x >= m or y >= m):
    			print "0"
    			return
    		else:
    			print "-1"
    			return 
    
    	if(x < y) x,y = y,x
    	if(x >= m):
    		print "0"
    		return
    	else:
    		ans = 0
    		if(abs(y)%x==0):
    			ans = abs(y)/x
    			y = 0
    		else:
    			ans = abs(y)/x
    			ans +=1
    			y = y + (ans*x)
    		while(x < m and y < m):
    			if(x < y):
    				x,y = y,x
    			#x is greater
    			y = x+y
    			ans+=1
    		print ans
    
    	return
    if __name__ == "__main__":
    	solver()
    	