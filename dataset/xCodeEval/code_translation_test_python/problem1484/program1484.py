def program1484():
    from sets import Set
    s=input()
    a=Set()
    n=10
    res = 1
    for i in range(len(s)):
    	if s[i] == '?':
    		if i == 0:
    			res *= 9
    		else:
    			res *= 10
    	elif s[i] >= 'A' and s[i] <= 'Z':
    		if s[i] not in a:
    			if i == 0:
    				res *= 9
    			else:
    				res *= n
    			if n > 0:
    				n = n-1
    			a.add(s[i])
    print(res)