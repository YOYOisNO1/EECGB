def program4112():
    from sys import stdin
    
    
    p, k = stdin.readline().rstrip().split(' ')
    p = int(p); k = int(k)
    
    if k==0:
    	print(((p)**(p-1)) % (10**9+7))
    
    elif k==1:
    	print((p**p) % (10**9+7))
    
    else:
    	free = set(range(1, p))
    	loops = 0
    
    	while free:
    		n = free.pop()
    		l = (n*k)%p
    		while l != n:
    			free.remove(l)
    			l = (l*k) % p	
    		loops += 1
    
    
    	print(p**loops % (10**9+7))