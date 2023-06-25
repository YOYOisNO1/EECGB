    n = int(input());
    
def f(n):
    	while n > 360 : n -= 360;
    	while n < 0 : n += 360	
    	return min(min(n,abs(360-n)),56565);
    
    B = f(n);
    cost = 0;
    if n < 0: 
    	n = -n;
    	B,cost = f(n),0;
    elif n > 0:
    	n = 360 - n;
    	B,cost = f(n),0
    
    ctr = -1;
    m = n;
    for i in xrange(5):
    	ctr += 1;
    	n = m + i * 90;
    	if f(n) < B:
    		B = f(n);
    		cost = ctr;
    
    ctr = -1
    for i in xrange(5):
    	ctr += 1;
    	n = m - i * 90;
    	if f(n) < B:
    		B = f(n);
    		cost = min(cost,ctr);
    
    	
    print cost