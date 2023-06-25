def nod(a, b):
    	a = int(a)
    	b = int(b)
    	if(a > b):
    		a, b = b, a
    	if(b % a == 0):
    		return a
    	else:
    		while(b != 0):
    			if(a > b):
    				a, b = b, a
    			x = b // a
    			b -= x * a
    		return a
    
    s = input()
    s = s.split()
    
    a = int(s[0])
    b = int(s[1])
    x = int(s[2])
    y = int(s[3])
    
    q = nod(x, y)
    x = x // q
    y = y //q
    
    if(a > b):
    	a, b = b, a
    	x, y = y, x
    
    i = a
    
    while i * y // x > b:
    	i -= 1
    
    
    
    print(i // x)