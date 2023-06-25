def program936():
    x,y = map(int,input().split())
    n = input()
    m = (10**9) + 7
    
    if n == 1:
    	print(x%m)
    elif n == 2:
    	print(y%m)
    else:
    	t = n / 3
    	u = n % 3
    	if t&1:
    		if u == 0:
    			print((y) - x) % m 
    		elif u == 1:
    			print(-x%m)
    		else:	
    			print(-y) % m
    	else:
    		if u == 0:
    			print((x) - y)%m
    		elif u == 1:
    			print(x%m)
    		else:	
    			print(y%m)