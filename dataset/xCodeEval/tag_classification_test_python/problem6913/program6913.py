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
    z=n+n-1
    if z==10**len(str(n))-1:
    	print(1)
    elif len(str(n))==1:
    	if n>4:
    		print(min(n-4,4))
    	else:
    		print((n*(n-1))/2)
    #	print(max(0,n-4))
    else:
    	small=(10**(len(str(z))-1))-1
    	large=z
    	if (large-small)%(10**(len(str(z))-1))!=0:
    		large=small+((large-small)/(10**(len(str(z))-1)))*(10**(len(str(z))-1))
    	ans=0
    	i=small
    	while i<=large:
    		ans+=min(i/2,n-i/2)
    		#print(i,n,ans)
    		i+=(10**(len(str(z))-1))
    	print(ans)
    
    	#9+4+