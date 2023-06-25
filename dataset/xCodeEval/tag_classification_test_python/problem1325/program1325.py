def program1325():
    #import sys
    #sys.stdin = open('in.txt', 'r')
    L = 1
    R = 1
    (n, k, m, d) = map(int, input().split())
    A = 1
    for i in xrange(1, d + 1):
    	ans = 0
    	l = 1
    	r = m
    	mid = int((l + r) //2)
    	while(l <= r):
    		mid = int((l + r) // 2)
    		if((n / mid) <= i * k):
    			ans = mid
    			r = mid - 1
    		else:
    			l = mid + 1
    	L = ans
    	if(ans == 0):
    		continue
    	ans = 0
    	l = 1
    	r = m
    	mid = int((l + r ) // 2)
    	while(l <= r):
    		mid = int((l + r) // 2)
    		if((n / mid) > k * i - k):
    			ans = mid
    			l = mid + 1
    		else:
    			r = mid - 1
    	if(ans == 0):
    		continue	
    	R = ans
    	if(L <= R and A < R * i):
    		A = R * i
    	#print(L,)
    	#print(R)
    print(A)