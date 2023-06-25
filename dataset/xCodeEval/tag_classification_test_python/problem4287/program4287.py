def program4287():
    n, l, r, x = map(int, input().split(" "))
    problems = map(int, input().split(" "))
    
    ways = 0
    
    for zz in xrange(1, 2 ** n):
    	i = zz
    	start = -1
    	last = -1
    	tot = 0
    	j = 0
    	while (start < 0):
    		if (i % 2 == 1):
    			start = problems[j]
    			last = problems[j]
    			tot = problems[j]
    		j += 1
    		i /= 2
    
    	while (i > 0):
    		if (i % 2 == 1):
    			tot += problems[j]
    			if problems[j] < start:
    				start = problems[j]
    			if problems[j] > last:
    				last = problems[j]
    		j += 1
    		i /= 2
    
    	if last - start >= x and tot <= r and tot >= l:
    		ways += 1
    
    print(ways)