def program5899():
    import math
    import string
    import itertools
    from random import *
    import fractions
    
    n = int(input())
    crush = map(int, input().split())
    
    #n = 4
    #crush = [2,3,1,4]
    s = set()
    flg = 0
    for i in crush:
    	if i in s:
    		print(-1)
    		flg = 1
    		break
    	else:
    		s.add(i)
    
    if flg == 0:
    	for i in range(n):
    		crush[i] -= 1
    
    	lis = []
    	for i in range(n):
    		j = i
    		idou = 0
    		while True:
    			k = crush[j]
    			idou += 1
    			if i == k:
    				lis.append(idou)
    				break
    			j = k
    
    	ans = 0
    	s = []
    	for i in lis:
    		if i%2 == 0 and i/2 not in s:
    			s.append(i/2)
    		elif i%2 == 1 and i not in s:
    			s.append(i)
    	print(reduce(lambda) x,y:x*y/fractions.gcd(x,y),s)