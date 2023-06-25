def program2842():
    n = input()
    s = input().strip()
    ans = "no"
    l = 0
    if s.count("*") < 5:
    	print(ans)
    	exit()
    while ans == "no" and l <= n/4:
    	# print(l+1)
    	a = 0
    	b = a+l+1
    	c = b+l+1
    	d = c+l+1
    	e = d+l+1
    	while ans == "no" and e < n:
    		x = s[a] + s[b] + s[c] + s[d] + s[e]
    		# print(x,a,b,c,d,e)
    		cc = x.count("*")
    		if cc == 5:
    			ans = "yes"
    			break
    		a += 1
    		b = a+l+1
    		c = b+l+1
    		d = c+l+1
    		e = d+l+1
    	l += 1
    print(ans)