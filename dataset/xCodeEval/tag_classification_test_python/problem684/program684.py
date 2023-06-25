def program684():
    '''input
    30 20 10
    '''
    a = map(int, input().split())
    
    res = sum(a)
    for meet in xrange(min(a), max(a) + 1):
    	res = min(res, sum([abs(x - meet) for x in a]))
    
    print(res)