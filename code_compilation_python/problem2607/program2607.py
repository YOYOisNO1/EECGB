def rolling(w,h,u1,d1,u2,d2):
    	w_new = w
    	while h>=0:
    		w_new += h
    		
    		if h==d1:
    			w_new -=u1
    			if w_new < 0:
    				w_new = 0
    			h -= 1
    		
    		elif h==d2:
    			w_new -= u2
    			if w_new < 0
    				w_new = 0
    			h-=1
    
    		else:
    			h-=1
    	print(w_new)
    
    w,h = map(int, input().split())
    u1,d1 = map(int, input().split())
    u2,d2 = map(int, input().split())}
    rolling(w,h,u1,d1,u2,d2)