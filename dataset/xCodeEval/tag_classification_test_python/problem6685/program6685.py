    import math
    
def count_factors(n, p):
    	result = 0
    	while n>=p:
    		n//=p
    		result += n
    	return result
    
    n, b = map(int, input().split())
    
    m = math.inf
    for p in range(2, int(math.sqrt(b))+1):
    	power = 0
    	while b%p==0:
    		power += 1
    		b//=p
    	if power!=0:
    		m = min(m, count_factors(n, p)//power)
    
    if b>1:
    	m = min(m, count_factors(n, b))
    print(m)