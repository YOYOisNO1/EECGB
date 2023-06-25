def program1168():
    k = int(input())
    if k == 0:
    	print("a")
    
    else:
    
    	char = 97
    
    	while k > 0:
    
    		x = 2
    		while (x * (x + 1)) // 2 < k:
    			x += 1
    
    		k = k - ((x * (x - 1)) //2)
    		
    		print(chr(char) * x,end='')
    
    		char += 1