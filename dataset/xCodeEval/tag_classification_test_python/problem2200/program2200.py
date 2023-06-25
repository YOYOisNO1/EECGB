def program2200():
    from math import sqrt
    n = int(input())
    r = 0
    for i in range(1,n):
    	for j in range(i+1,n):
    
    		t = i*i + j*j 
    		if t > n*n:
    			break
    		if sqrt(t) == int(sqrt(t)):
    			r = r + 1
    print(r)