def program85():
    R = lambda :list(map(int,input().split()))
    a,b,f,k = R()
    p = b
    s = 0
    
    if k == 1  :
    	if f > b or (a-f) >b :
    		print(-1)
    	else :
    		if b >= a :
    			print(0)
    		else :
    			print(1)
    elif k == 2 :
    	if (b < 2*(a-f)) or  (b < f) :
    		print(-1)
    	else :
    		if b >= 2*a :
    			print(0)
    		elif b >= a + a - f :
    			print(1)
    		elif b >= a + f :
    			print(1)
    		else :
    			print(2)
    
    
    
    else :
    
    
    
    	if b < 2*(a-f) or b < 2*f  :
    		print(-1)
    	else :
    		for i in range(k) :
    			if i == k-1 :
    				if b < a :
    					s += 1
    			else :
    				if i%2 == 0 :
    					if b >= a + a - f :
    						b -= a 
    					else :
    						s += 1
    						b = p -(a-f)
    				else :
    					if b >= a + f :
    						b -= a 
    					else :
    						b = p -f
    						s += 1
    
    
    
    		print(s)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    