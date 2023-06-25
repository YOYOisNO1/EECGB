    from math import gcd
    
def factors(k):
    	for i in range(1, int(k ** 0.5)):
    		if k % i == 0:
    			j = k // i
    			yield i
    			if i != j: yield j
    
    x, y = map(int, input().split())
    d = y - x
    
    ml = float("inf")
    mo = 0
    
    for q in factors(d):
    	o = (q - (x % q)) % q
    	lcm = (x + o) * (y + o) // gcd(x + o, y + o)
    	if lcm < ml:
    		ml = lcm
    		mo = o
    
    print(mo)