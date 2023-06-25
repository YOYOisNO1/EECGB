def program2566():
    n, a, x, b, y = map(int, input().strip().split())
    ai, bi = a, b
    if ai == bi:
    	exit(print('YES'))	
    while True:
    	ai = 1 if ai+1 > n else ai+1 
    	bi = n if bi-1 < 1 else bi-1 
    	if ai == bi:
    		exit(print('YES'))
    	if ai == x or bi == y:
    		break
    print('NO')