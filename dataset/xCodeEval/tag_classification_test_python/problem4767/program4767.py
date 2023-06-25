    from math import sqrt
def SQRT(x):
    	u = int(sqrt(x)) + 2
    	while u*u > x: u -= 1
    	return u
    
    
    P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89, 97]
    
def split(x, i = 0):
    	ret = 10**20
    	if x < 64: ret = P[i]**(x-1)
    	d = 2
    	while d**2 <= x and d <= 64:
    		if x%d:
    			d += 1
    			continue
    
    		q = P[i]**(d-1)
    		if q < ret: ret = min(ret, q * split(x//d, i+1))
    		q = P[i]**(x//d - 1)
    		if q < ret: ret = min(ret, q * split(d, i+1))
    		d += 1
    	return ret
    
    n = int(input())
    if n == 1: print(1)
    else: print(split(n))
    