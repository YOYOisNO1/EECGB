def program5621():
    
    n,m=map(int, input().split(' '))
    
    
    
    	
    if n==1 or m==1 or (n==2 or m==2):
    	if n==1 or m==1:
            	print(n*m)
    	else:
    		if n*m%4!=0:
    			print(n*m/2+1)
    		else:
    			if  n*m%8==0:
    				print(n*m/2)
    			else:
    				print((n*m/8+1)*4)
    	
    
    
    else:
    	if n*m%2==0:
    		print(n*m/2)
    	else:
    		print(n*m/2+1)
    