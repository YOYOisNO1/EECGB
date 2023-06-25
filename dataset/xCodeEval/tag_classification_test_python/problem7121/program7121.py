    import math
    
def expmod(base, expon, mod):
        ans = 1
        for i in range(1, expon + 1):
    	    ans = (ans * base) % mod
        return ans
    
    p, k = input().split()
    s = 10 ** 9 + 7
    k = int(k)
    p = int(p)
    ord = 1
    done = 0
    if k == 0:
    	z = p - 1
    if k == 1:
        z = p
    else:
    	for i in range(2,p + 1):
    		if done == 0:
    			if (p-1) % i == 0:
    				if expmod(k, i, p) == 1:
    					ord = i
    					done = 1
    	z = int((p-1) / ord)
    rem = expmod(p, z, s)
    print(int(rem))