    n, p = input().split()
    
    p = float(p)
    n = int(n)
    
def cnk(n, k):
    	if n < k:
    		return 0
    	ret = 1
    	if(k == 1):
    		return n
    	if k == 2:
    		return n * (n - 1) // 2
    	return n * (n - 1) * (n - 2) // 6
    
    for i in range(0, n + 1):
    	cur_prob = 0.0
    	
    #	ca = i / n * (n - i) / n * (n - i - 1) / n
    	ca = cnk(i, 1) * cnk(n - i, 2) / cnk(n, 3)
    	ca = ca * 3 / 6
    	
    #	cb = i / n * (i - 1) / n * (n - i) / n
    #	cb = cb / 2
    	cb = cnk(i, 2) * cnk(n - i, 1) / cnk(n, 3)
    	cb = cb
    #	cc = i / n * (i - 1) / n * (i - 2) / n
    #	cb = cb
    	cc = cnk(i, 3) / cnk(n, 3)
    	cur_prob = ca + cb + cc
    #	print(cur_prob)
    	if(cur_prob >= p):
    		print(i)
    		break;