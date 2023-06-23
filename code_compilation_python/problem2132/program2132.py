def program2132():
    
    n = int(input())
    '''
    l = []
    
    for _ in range(4):
    	l.extend(list(input()))
    
    dots = l.count('.')
    for _ in range(dots):
    	l.remove('.')
    
    
    for i in set(l):
    	if l.count(i) > 2 * n:
    		print('NO')
    		exit()
    
    print('YES')
    '''
    
    from collections import defaultdict
    
    d = defaultdict(int)
    
    for _ in range(4):
    	l = list(input())
    	for i in l:
    		if i != '.':
    			d[i] += 1
    
    if max(d.values()) > 2 * n:
    	print('NO')
    else:
    	print('YES')