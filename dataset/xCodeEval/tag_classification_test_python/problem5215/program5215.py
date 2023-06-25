    import sys
    from math import *
    
def minp():
    	return sys.stdin.readline().strip()
    
def mint():
    	return int(minp())
    
def mints():
    	return map(int, minp().split())
    
    Z = 1179859
    isprime=[True]*Z
    isprime[1] = False
    for i in range(2,Z):
    	if isprime[i]:
    		for j in range(i*i,Z,i):
    			isprime[j] = False
    
    p, q = mints()
    cnt1 = 0
    cnt2 = 0
    r = -1
    for i in range(1,Z):
    	if isprime[i]:
    		cnt1 += 1
    	if str(i) == str(i)[::-1]:
    		cnt2 += 1
    	if cnt1 <= cnt2*p/q:
    		r = i
    print(r)