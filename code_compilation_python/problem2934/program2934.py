def program2934():
    '''
    21st august 2017 monday
    codeforces 825b
    '''
    from sys import stdin
    
    t = map(int, list(stdin.readline().strip()))
    
    sum_left = sum(t[:3])
    sum_right = sum(t[3:])
    
    if sum_left == sum_right:
    	print 0
    elif sum_left < sum_right:
    	d = sum_right - sum_left
    	for i in xrange(3):
    		t[i] = 9 - t[i]
        '''
        for i in xrange(3, 6):
    		t[i] = t[i] - 1
        '''
    	print t, d
    	t.sort(reverse=True)
    	i = 0
    	while d > 0:
    		d -= t[i]
    		i += 1
    	print i
    else:
    	d = sum_left - sum_right
    	for i in xrange(3, 6):
    		t[i] = 9 - t[i]
        '''
    	for i in xrange(3):
    		t[i] = t[i] - 1
        '''
    	t.sort(reverse=True)
    	i = 0
    	while d > 0:
    		d -= t[i]
    		i += 1
    	print i