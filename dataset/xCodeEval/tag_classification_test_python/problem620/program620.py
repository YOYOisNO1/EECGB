    from fractions import gcd
    from math import factorial, ceil, sqrt, atan2
    from itertools import *
    import string
    import copy
    import random
    import bisect
    from decimal import *
def id_generator(size=20, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
     
def mp():
        return map(int,str(input()).split())
    
    n=input()
    l=list(mp())
    z=[31,29,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31,31,29,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31]
    flag=0
    for i in range(len(z)-n):
    	if z[i:i+n]==l:
    		flag=1
    if flag:
    	print('YES')
    else:
    	print('NO')