def program2923():
    x, y = map(int, input().split())
    
    ch = ['A', 'B']
    s = []
    b = 0
    if x < y:
    	b = 1
    	x = x^y; y = x^y; x = x^y
    if y!=1 and x%y == 0:
    	print 'Impossible'
    else:
    	while y!=0:
    		l = x//y
    		s.append(l)
    		r = x%y
    		x = y
    		y = r
    	s[-1]-=1
    	st = ''
    	for el in s:	
    		st += '{}{}'.format(el, ch[b])
    		b = 1-b
    	print st
    
    
    
    
    
    
    
    