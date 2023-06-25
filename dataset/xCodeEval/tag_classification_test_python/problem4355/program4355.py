def program4355():
    n,k = map(int,input().split())
    from math import sqrt
    from math import ceil
    x2 = float("inf")
    t = max(ceil(sqrt(n)),int(sqrt(n))+1)
    for i in range(int(sqrt(n)),0,-1):
    	r1,r2 = float("inf"),float("inf")
    	if i < k and n%i == 0:
    	
    		r1 = k*(n//i)+i
    	if k > n//i and n%(n//i) == 0:
    		r2 = k*i+n//i
    	
    	x2 = min(x2,r1,r2)
    print(x2)