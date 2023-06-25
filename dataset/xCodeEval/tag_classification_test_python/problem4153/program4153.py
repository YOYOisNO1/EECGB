def program4153():
    #coding:utf-8
    
    a, b = map (int, input ().split ())
    c = a+b
    ans = c*2+2
    
    x, y = 1, a
    xx, yy = 1, b
    index1, index2 = 1, 1
    i = 2
    while i*i <= c:
    	if c%i == 0:
    		while index1 <= i and index1 <= a:
    			if a%index1 == 0:
    				x, y = index1, a/index1
    			index1 += 1
    		if x <= i and y <= c/i:
    			ans = min (ans, 2*(i+c/i))
    
    		while index2 <= i and index2 <= b:
    			if b%index2 == 0:
    				xx, yy = index2, b/index2
    			index2 += 1
    		if xx <= i and yy <= c/i:
    			ans = min (ans, 2*(i+c/i))
    	i += 1
    
    
    print(ans)
    
    
    
    
    '''
    5*7
    4*6
    '''
    
    
    
    
    
    
    