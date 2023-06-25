def program2930():
    n = input()
    
    dx = [1, -1, -2, -1, 1, 2]
    dy = [2, 2, 0, -2, -2, 0]
    
    low = 0
    high = 10 ** 18
    
    while high - low > 1:
    	mid = (low + high) / 2
    	num = 3 * mid * (mid + 1) - mid
    	if n >= num:
    		low = mid
    	else:
    		high = mid
    
    x = -dx[1] * low
    y = -dy[1] * low
    
    n -= 3 * low * (low + 1) - low
    
    for i in xrange(6):
    	use = 0
    	if i != 1:
    		use = min(n, low + 1)
    	else:
    		use = min(n, low)
    	n -= use
    	x += dx[i] * use
    	y += dy[i] * use
    
    print(x,) y
    