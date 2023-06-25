    import math
    
def gcd(a, b):
    	return gcd(b, a % b) if b else a
    
    x, y, n = [int(i) for i in input().split(' ')]
    
    p = (x + .0) / y
    epsnum, epsden = x, n
    a, b = 0, 0
    
    for i in range(1, n + 1):
    	j = int(math.floor(i * p))
    	curepsnum, curepsden = abs(x * i - y * j), y * i
    	diff = curepsnum * epsden - curepsden * epsnum
    	if diff < 0L:
    		epsnum, epsden, a, b = curepsnum, curepsden, j, i
    
    	j = int(math.ceil(i * p))
    	curepsnum, curepsden = abs(x * i - y * j), y * i
    	diff = curepsnum * epsden - curepsden * epsnum
    	if diff < 0L:
    		epsnum, epsden, a, b = curepsnum, curepsden, j, i
    
    g = gcd(a, b)
    print("%d/%d") % (a / g, b / g)