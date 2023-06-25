def program3160():
    
    n,m = [int(c) for c in input().split()]
    if n == 1:
    	print(1)
    else:	
    	if m>n-m:
    		print(m-1)
    	else:
    		print(m+1)