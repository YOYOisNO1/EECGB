    from fractions import gcd
    from math import factorial, ceil, sqrt, atan2, log, pi, e
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
    
    a,b,p,x=mp()
    ans=0
    inv_mod=pow(a,p-2,p)
    d=-b
    bla=p*(p-1)
    
    for i in range(p-1):
    	val=(d+i)%p
    	val*=(p-1)
    	val=x-i-val
    	ans+=val/bla+1
    	d*=inv_mod
    	d%=p
    
    print(ans)