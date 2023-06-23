    import time
def get_num(w,h):
    	counter=0
    	tmp=0
    	x=False
    	while (x==False):
    		print 'start:',w,h
    		if w==h:
    			x=True
    		w=w-h
    		
    		if w<h:
    			tmp=w
    			w=h
    			h=tmp
    		print 'end:',w,h
    		time.sleep(5)
    		counter+=1
    	
    	return counter
    
    
    
    a,b=map(int,input().split(" "))
    print get_num(a,b)