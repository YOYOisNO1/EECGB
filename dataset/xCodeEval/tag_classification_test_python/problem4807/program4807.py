def program4807():
    from math import ceil,floor
    
    from math import sqrt
    n=int(input())
    l=sqrt(n)
    if ceil(l)==floor(l):
    	print(int(4*l))
    else:
    	g1=ceil(l)
    	g2=floor(l)
    	m=(g1+g2)/2
    	if l>=m:
    		print(ceil(l)*4)
    	else:
    		print((ceil(l)+floor(l))*2)
    		
    
    
    
    