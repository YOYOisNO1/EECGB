def check():
    	global L
    	for i in xrange(0, len(L)):
    		if L[i] > 1:
    			return i
    	return -1
    
def func(n):
    	global L
    	L = [int(n)]
    
    	while True:
    		index = check()
    		if index < 0:
    			break
    		x = L[index]
    		L = L[:index] + [x / 2, x % 2, x / 2] + L[(index + 1):]
    
    	return L
    
    #if len(sys.argv) >= 2:
    #	n = sys.argv[1]
    #	print(func(n))
    
    #for n in xrange(1, 30):
    #	LL = func(n)
    #	print(n,) len(LL), LL.count(1)
    
def llen(n):
    	p = 1
    	while p <= n:
    		p *= 2
    	return p - 1
    
def naive(n, l, r):
    	LL = func(n)
    	return LL[l:(r + 1)].count(1)
    
def fuunc(n, l, r, reclvl = 0):
    	#print('-') * reclvl + str(n), l, r
    	if l > r or n == 0:
    		#print('-') * reclvl + 'returned', 0
    		return 0
    
    	L = llen(n)
    	if r >= L:
    		r = L
    
    	if (r - l + 1) == L:
    		#print('-') * reclvl + 'returned', n
    		return n
    
    	mid = L / 2
    	rest = n % 2
    
    	if r <= mid:
    		ans = 0
    		if r == mid:
    			ans += rest
    			r -= 1
    		retval = fuunc(n / 2, l, r, reclvl + 1) + ans
    		#print('-') * reclvl + 'returned', retval
    		return retval
    	if l >= mid:
    		ans = 0
    		if l == mid:
    			ans += rest
    			l += 1
    		retval = fuunc(n / 2, l - mid - 1, r - mid - 1, reclvl + 1) + ans
    		#print('-') * reclvl + 'returned', retval
    		return retval
    	
    	retval = fuunc(n / 2, 0, r - mid - 1, reclvl + 1)	+ fuunc(n / 2, l, L / 2 - 1, reclvl + 1) + rest
    	#print('-') * reclvl + 'returned', retval
    	return retval
    
    params = input().split(' ')
    print(fuunc(int(params[0]),) int(params[1]) - 1, int(params[2]) - 1)
    #print(naive(int(params[0]),) int(params[1]) - 1, int(params[2]) - 1)