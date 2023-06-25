def program2230():
    '''input
    2
    '''
    from sys import stdin
    import math
    
    # main starts
    n = int(stdin.readline().strip())
    root = int(math.sqrt(n))
    if root ** 2  == n:
    	print(2 * root)
    	exit()
    else:
    	t = root * 2
    	count = root ** 2
    	if n - count <= root:
    		t += 1
    	elif n - count > root and n - count <= 2 * root + 1:
    		t += 2
    	print(t)
    	exit()