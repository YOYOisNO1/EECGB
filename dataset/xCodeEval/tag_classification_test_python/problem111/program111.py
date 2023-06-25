    import io, sys, atexit, os
    import math as ma
    from sys import exit
    from decimal import Decimal as dec
    from itertools import permutations
    from random import randint as rand
    
    
def li ():
    	return list (map (int, input ().split ()))
    
    
def num ():
    	return map (int, input ().split ())
    
    
def nu ():
    	return int (input ())
    
    
def find_gcd ( x, y ):
    	while (y):
    		x, y = y, x % y
    	return x
    
    
def lcm ( x, y ):
    	gg = find_gcd (x, y)
    	return (x * y // gg)
    
    
    mm = 1000000007
    yp = 0
    
    
def solve ():
    	t = 1
    	for _ in range (t):
    		n,h,m=num()
    		a=[99999999]*(n+2)
    		for i in range(m):
    			x,y,z=num()
    			for j in range(x,y+1):
    				a[j]=min(a[j],z*z)
    		ss=0
    		for i in range(1,n+1):
    			if(a[i]== 99999999):
    				ss+=h*h
    			else:
    				ss+=a[i]
    		print(ss)
    
    
    
    if __name__ == "__main__":
    	solve ()