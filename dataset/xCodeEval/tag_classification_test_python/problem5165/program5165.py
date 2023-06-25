def program5165():
    n , l ,r = map(long , input().strip().split())
    st = n
    f = []
    while st > 1:
    	f.append(st)
    	st /= 2
    if n == 0:
    	print(0)
    	exit(0)
    
    cnt = len(f)
    tot = (r-l+1)
    vis = dict()
    for i in f:
    	to = 2 ** cnt
    	ix = l
    	while (ix < r+1):
    		if ix % to == 0 and ix not in vis:
    			vis[ix] = True
    			if i % 2 == 0:
    				tot -= 1
    		ix += 1
    	cnt -= 1
    
    print(tot)