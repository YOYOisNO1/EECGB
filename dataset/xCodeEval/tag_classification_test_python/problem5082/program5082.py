def program5082():
    import math
    n,a,b,c,d = input().split()
    n=int(n)
    a=int(a)
    b = int(b)
    c=int(c)
    d=int(d)
    sum =0
    g = 0
    for x in range(1,n+1):
    	y = x + b -c
    	z = x + a - d 
    	w = z + b -c
    	if((1<=y<=n)):
    		if((1<=z<=n)):
    			if(1<=w<=n):
    
    				sum += 1
    g = n * sum
    print((g))