def program1323():
    n, m = map(int, input().split())
    
    count = 0
    while m > n:
    	if m == 2*n:
    		n = m
    	elif m%2:
    		m += 1
    	else:
    		m = m//2
    
    	count += 1
    
    count += n-m
    
    print(count)