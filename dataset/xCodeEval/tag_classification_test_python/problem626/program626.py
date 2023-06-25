def program626():
    x = input()
    s = input()
    res = []
    max = 0
    
    for l in s:
    	#print((l))
    	if l >= 'a' and l <= 'z':
    		if res.count(l) == 0:
    			res.append(l)
    			if len(res) > max:
    				max = len(res)
    	else:
    		res = []
    
    print(max)