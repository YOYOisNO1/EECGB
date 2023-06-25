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
    if m==0:
    	print(n,n)
    	exit()
    else:
    	x=0
    	while (x*(x+1))/2 < m:
    		x=x+1
    
    	print(max(0,n-2*m),max(n-x-1,0))