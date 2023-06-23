def program3411():
    #coding:utf-8
    
    a, b = map (int, input ().split ())
    c = a+b
    ans = c*2+2
    
    x, y = 1, a
    index = 1
    i = 2
    while i*i <= c:
    	if c%i == 0:
    		while index <= i:
    			if a%index == 0:
    				x, y = index, a/index
    			index += 1
    		if x <= i and y <= c/i:
    			ans = min (ans, 2*(i+c/i))
    	i += 1
    
    
    print ans
    
    
    
    
    
    
    
    
    
    
    
    