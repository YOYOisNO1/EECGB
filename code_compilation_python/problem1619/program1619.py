def program1619():
    x = int(input())
    y = int(input())
    z = int(input())
    
    a = int(input())
    b = int(input())
    c = int(input())
    
    if x > a:
    	print('NO')
    	return
    else:
    	a -= x
    
    if y > a + b:
    	print('NO')
    	return
    else:
    	if a < y:
    		y -= a
    		a = 0
    	b -= y
    
    if z > a + b + c:
    	print('NO')
    else:
    	print('YES')