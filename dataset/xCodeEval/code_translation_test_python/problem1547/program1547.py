def program1547():
    from sys import stdin
    
    
    c = 10**9+7
    p, k = stdin.readline().rstrip().split(' ')
    p = int(p); k = int(k)
    
    if k==0:
    	print(pow(p, p-1, c))
    
    elif k==1:
    	print(pow(p, p, c))
    
    else:
    	n = k
    	order = 1
    	while n != 1:
    		n = (n*k) % p
    		order += 1
    	loops = (p-1) // order
    	print(pow(p, loops, c))