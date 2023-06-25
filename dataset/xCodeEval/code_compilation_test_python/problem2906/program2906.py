    '''input
    1 2 1 2
    
    
    '''
    
    from collections import defaultdict as df
    from bisect import bisect_left as bl 
    from itertools import combinations as c
    import sys
    from math import *
    from random import randint as R
    import heapq as hp
    
    l,r,a,b=[int(x) for x in input().split()]
    
    num=a*b
    
    p=[]
    c=0
def gcd(a,b):
    	if b==0:
    		return a
    	return gcd(b,a%b)
    
    for i in range(max(1,a),int(num**0.5)+1):
    	if num%i==0:
    		if l<=i<=r and l<=num/i<=r:
    			if gcd(i,num/i)==a and (a*b)/gcd(i,num/i)==b:
    				c+=2
    				#print i,num/i
    				if i*i==num:
    					c-=1
    print c
    
    
    
    
    
    
    
    
    