def program1194():
    
     n=int(input())
    z=19
     
    while n>1:
    	z=z+9
    	a =  sum(map(int,str(z)))
    	
    	if a == 10:
    		n=n-1
    		
    print (z)