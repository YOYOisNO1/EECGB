def program665():
    '''input
    AAA
    '''
    vowels = 'AEIOUY'
    last = 0
    res = 0
    
    s = 'X' + input() + 'A'
    for i in xrange(len(s)):
    	ch = s[i]
    	if ch in vowels:
    		res = max(res, i - last)
    		last = i
    
    print(res)