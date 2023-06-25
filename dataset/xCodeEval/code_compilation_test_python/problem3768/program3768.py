def pow_mod(a,sup,m):
    	ans = 1
    	while sup > 0:
    		if sup & 1: ans = (ans*a) % m
    		a = a*a % m
    		sup >>= 1
    	return ans
    
    a, b, p, x = [int(t) for t in input().split()]
    inv = [0] * p	
    ans = 0
    for i in xrange(1,p):
    	w = pow(a,i,p)
    	r, s = (p-1)*w%p, (b-i*w)%p
    	if r == 0:
    		if s: 
    			ans += x/(p-1)
    			if x%(p-1)>=i:
    				ans += 1
    		#print i, ans, r, s, 'a'
    		break
    	if not inv[r]:
    		inv[r] = pow_mod(r, p-2, p)
    		inv[inv[r]] = r
    	k = s*inv[r]%p
    	y = (x-i-k*(p-1))/(p*(p-1))
    	if y >= 0:
    		ans += y+1
    	#print i, ans, r, s, 'b', k
    print ans