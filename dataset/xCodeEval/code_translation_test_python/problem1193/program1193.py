def win():
    	for i in xrange(4):
    		for j in xrange(4):
    			if a[i][j] != 'x':
    				continue;
    			if i > 1:
    				if a[i - 2][j] == 'x' and a[i - 1][j] == 'x':
    					return True
    			if j > 1:
    				if a[i][j - 1]  == 'x' and a[i][j - 2] == 'x':
    					return True
    			if i > 1 and j > 1:
    				if a[i - 1][j - 1] == 'x' and a[i - 2][j - 2] == 'x':
    					return True
    			if i > 1 and j + 2 < 4:
    				if a[i - 1][j + 1] == 'x' and a[i - 2][j + 2] == 'x':
    					return True
    	return False
    a = []
    for i in xrange(4):
    	a.append(list(input()))
    #print(a)
    for i in xrange(4):
    	for j in xrange(4):
    		if a[i][j] == '.':
    			a[i][j] = 'x'
    			if win():
    				print('YES')
    #	print("i = %d j = %d") %(i, j)
    				exit(0)
    			a[i][j] = ','
    print('NO')