def program2513():
    import string
    n = int(input())
    
    colors = "ROYGBIV"
    
    res = ['R', 'O', 'Y'] + [' '] * (n-3)
    
    c = 3
    
    left = n-1
    right = 3
    
    while left>right:
    	if(left-right>3):
    		res[left] = colors[c]
    		res[right] = colors[c]
    		c = (c+1) % 7
    		left -= 1
    		right += 1
    	else:
    		for j in range(left-right+1):
    			res[left] = colors[c]
    			c = (c+1) % 7
    			left -= 1
    
    print string.join([i for i in res], '')
    
    
    		