def program327():
    a,b = map(int,input().split())
    k = 0;
    while (min(a,b)>0): 
    	if ( b < a ):
    		k += a//b
    		a -= b*(a//b)
    		
    	else:
    		k += b//a
    		b -= a*(b//a)		
    
    print(k)	