def program4048():
    a, b = map(int, input().split())
    moves = []
    moves.append(b)
    while(b>a):
    	if b%2==0:
    		b = int(b/2)
    		moves.append(b)
    	else:
    		if str(b)[-1]=='1':
    			b = int(str(b)[:-1])
    			moves.append(b)
    		else:
    			break
    
    
    if b!=a:
    	print('NO')
    else:
    	print('YES')
    	print(len(moves))
    	for i in range(len(moves)-1,-1,-1):
    		print(moves[i])