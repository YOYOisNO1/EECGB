def program3665():
    from math import sqrt
    
    for _ in xrange(int(input())):
    	a = map(int, input().split())
    	ok = True
    	if max(a) - min(a) != 1:
    		print("NO")
    		continue
    	x = a[0] + a[1]
    	cnt = 0
    	i = 2
    	while i * i <= x:
    		if x % i == 0:
    			cnt += 1
    		if cnt > 1: break
    		i += 1
    	if cnt == 0: print("YES")
    	else: print("NO")