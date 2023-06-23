def program243():
    from math import *
    from collections import *
    import sys
    sys.setrecursionlimit(10**9)
    
    mod = 10**9 + 7
    n,x = map(int,input().split())
    #for y in range(1):
    a = [0 for i in range(n+1)]
    ans = 0
    for i in range(1,n+1):
    	j = i
    	while(j >= 1):
    		a[j] += 1
    		if(j%2 == 0):
    			j //= 2
    		else:
    			j -= 1
    for i in range(n,0,-1):
    	if(a[i] >= x):
    		print(i)
    		break
    