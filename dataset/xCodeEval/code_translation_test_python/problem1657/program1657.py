    from fractions import gcd
    from math import factorial, ceil, sqrt, atan2, log, pi, e, asin,acos, cos, sin, floor
    from itertools import *
    from fractions import Fraction
    import string
    import copy
    import random
    import bisect
    from decimal import *
    from collections import deque
    from sys import *
    digs = string.digits + string.ascii_letters
    
def id_generator(size=20, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
     
def mp():
        return map(int,str(input()).split())
    
    
    n,m=mp()
    if n>m:
    	n,m=m,n
    if n==1:
    	if m%6==1:
    		print(m-1)
    	elif m%6==2:
    		print(m-2)
    	elif m%6==3:
    		print(m-3)
    	elif m%6==4:
    		print(m-2)
    	elif m%6==5:
    		print(m-1)
    	else:
    		print(m)
    	exit()
    
    if n==2:
    	total=m*n
    	if m==1 or m==3 or m==7:
    		print(total-2)
    	elif m==2:
    		print(total-4)
    	else:
    		print(total)
    	exit()
    
    
    print(n*m-((n*m)%2))
    #if (n%2==0 and m%2==0):
    #	print(n*m)
    #	exit()