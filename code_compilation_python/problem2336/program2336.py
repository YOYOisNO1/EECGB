def program2336():
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    
    c1 = 0
    
    if n%k == 0:
    	c2 = 0
    	t = [a[0], a[1]]
    	for i in range(k,n,k):
    		if a[i] != a[0]:
    			c2 += 1
    		if a[i+1] != a[1]:
    			c2 += 1
    print c2