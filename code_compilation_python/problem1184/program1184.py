def program1184():
    n,k,x = map(int, input().split())
    balls1 = map(int, input().split())
    if n == 1:
    	print 0
    	
    else:
    	contiguous = [1]
    	balls = [balls1[0]]
    	for i in xrange(n-1):
    		if balls1[i] == balls1[i+1]:
    			contiguous[-1] += 1
    		
    		else:
    			contiguous.append(1)
    			balls.append(balls1[i+1])
    
    	removes = []
    	for i in range(len(balls)):
    		if balls[i] == x and contiguous[i] == x:
    			removes.append(contiguous[i])
    			j = i-1
    			k = i+1
    			while j >= 0 and k < len(contiguous) and contiguous[j] + contiguous[k] >= x:
    				removes[-1] += contiguous[j] + contiguous[k]
    				j -= 1
    				k += 1
    			
    	print max(removes)