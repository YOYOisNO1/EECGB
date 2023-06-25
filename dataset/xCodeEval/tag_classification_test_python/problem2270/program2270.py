def program2270():
    import os, sys
    
    ri = lambda: input().strip()
    
    k = int(ri())
    l = int(ri())
    m = int(ri())
    n = int(ri())
    d = int(ri())
    
    result = 0
    
    if k == 1 or l == 1 or m == 1 or n == 1:
    	result = d
    else:
    	for x in range(1, d+1):
    		if (x % k == 0) or (x % l == 0) or (x % m == 0) or (x % n == 0):
    			result += 1
    
    print(result)