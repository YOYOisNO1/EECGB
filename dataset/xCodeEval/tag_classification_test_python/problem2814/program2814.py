def program2814():
    import sys
    
    s = input().split()
    n = s[0]
    k = int(s[1])
    c1 = c2 = 0
    i = len(n) - 1
    while i > 0 :
    	if n[i] == '0' :
    		c2 += 1
    		if c2 == k :
    			print(c1)
    			sys.exit()
    	else :
    		c1 += 1
    	i -= 1
    print(len(n)) - 1