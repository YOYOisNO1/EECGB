    from fractions import gcd
    from math import factorial, ceil, sqrt, atan2, log, pi, e, asin,acos, cos, sin, floor, atan
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
        return map(int,str(input()).strip().split())
    
    clear=stdout.flush()
    
    mod=10**9+7
    
def check(l, d, mid, n, m):
    	temp=[]
    	for i in range(n+1):
    		temp+=[l[i]]
    	earn=0
    	pre=[0 for i in range(n+1)]
    	for i in range(1,mid+1):
    		for j in d[i]:
    			pre[j]=i
    	d=[[] for i in range(mid+1)]
    	for i in range(n+1):
    		if pre[i]:
    			d[pre[i]]+=[i]
    	for i in range(1,mid+1):
    		earn+=1
    		for j in d[i]:
    			z=min(temp[j], earn)
    			earn-=z
    			temp[j]-=z
    		# print(temp,) earn, d[i], i
    	# print(mid,) earn, sum(temp)
    	if earn>=sum(temp)*2:
    		return 1
    	return 0
    
    n,m=mp()
    l=[0]+list(mp())
    d=[[] for i in range(500000+1)]
    for i in range(m):
    	a,b=mp()
    	d[a]+=[b]
    start=0
    end=500000
    while start<end:
    	mid=(start+end)/2
    	# print(mid)
    	if mid==start:
    		break
    	if check(l, d, mid, n, m):
    		end=mid
    	else:
    		start=mid+1
    
    # print(check(l,) d, 15, n ,m)
    if check(l , d, start, n , m):
    	print(start)
    else:
    	print(end)
    
    
    