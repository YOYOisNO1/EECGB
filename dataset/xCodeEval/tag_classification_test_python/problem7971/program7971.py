    import sys
    from math import *
    
def minp():
    	return sys.stdin.readline().strip()
    
def mint():
    	return int(minp())
    
def mints():
    	return map(int, minp().split())
    
    a,b,mod = mints()
    z = (10**9)%mod
    c = 0
    for i in range(min(a+1,mod)):
    	if c != 0 and mod-c > b:
    		s = str(i)
    		s = '0'*(9-len(s))+s
    		print(1, s)
    		exit(0)
    	c += z
    	if c >= mod:
    		c -= mod
    print(2)