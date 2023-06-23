def program2858():
    s = [int(x) for x in input().split()]
    x = s[0]
    y = s[1]
    l = s[2]
    r = s[3]
    
    v = [l - 1, r + 1]
    xx = 1
    yy = 1
    for i in range(64):
    	yy = 1
    	for j in range(64):
    		if(xx + yy <= r): 
    			v.append(xx + yy)
    			yy = y * yy	
    		else break
    	xx = xx * x;
    	
    sorted(v)
    
    
    ans = 0
    for i in range(len(v)):
    	ans = max(ans, v[i] - v[i - 1] - 1)
    	
    # your code goes here