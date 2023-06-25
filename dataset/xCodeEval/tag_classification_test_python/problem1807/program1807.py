def program1807():
    import math
    n = int(input())
    maxStep = 5
    if n <= 5:
    	print(1)
    
    elif n > maxStep:
    	
    	steps = math.ceil(n/5)
    	if steps < 3:
    		
    		if steps / maxStep-1 >= 3:
    
    			print(math.ceil(steps / maxStep-1))
    
    		elif steps / maxStep-1 < 3:
    			print(math.ceil(steps / maxStep -2))
    
    
    		elif steps / maxStep -2 < 3:
    			print(math.ceil(steps / maxStep -2))
    
    	elif steps  >= 3:
    		print(steps)