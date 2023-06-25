def flip(a):
    	b = [1-x for x in a]
    	return b
    n = input()
    a = map(int,input().split())
    if(n == 1 and a[0] = 0):
    	print 1
    elif(a.count(1) == n):
    	print n-1
    else:
    	ans = a.count(1)
    	for i in xrange(n):
    		for j in xrange(i,n):
    			f = 0
    			s = 0
    			t = 0
    			try:
    				f = a[:i].count(1)
    			except:
    				pass
    			try:
    				x = flip(a[i:j])
    				s = x.count(1)
    			except:
    				pass
    			try:
    				t = a[j:].count(1)
    			except:
    				pass
    			ans = max(ans, f+s+t)
    
    	print ans