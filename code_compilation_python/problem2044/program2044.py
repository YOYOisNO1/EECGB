def program2044():
    
    (a,b) = input().split()
    a = int(a)
    b = int(b)
    
    iter = int((10**4)*(10**0.5))
    for k in range(1, iter+1):
    	a_star = k ** 2
    	b_star = k * (k+1)
    
    	if a_star >= a:
    		return "Vladik"
    	if b_start >= b:
    		return "Valera"