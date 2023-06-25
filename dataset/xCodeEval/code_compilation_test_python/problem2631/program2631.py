def program2631():
    from itertools import product as prd
    
    n = int(input())
    l = [int(input()) for i in range(n)]
    
    s = '{}'.join(map(str, l))
    p = prd('+-', repeat = n)
    
    elif sum(l) >= 360:
    	for i in p:
    		if not eval(s.format(*i)) % 360:
    			print('YES')
    			break
    	else:
    		print('NO')
    else:
    	for i in p:
    		if not eval(s.format(*i)):
    			print('YES')
    			break
    	else:
    		print('NO')