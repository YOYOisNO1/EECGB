def program4957():
    Coins = 'ABC'
    n = 0
    C = ''
    D = {c:0 for c in Coins}
    for _ in range(3):
    	c = str(input())
    	if c[1] == '>':
    		D[c[0]]+=1
    	else:
    		D[c[2]]+=1
    for i in D:
    	if D[i]==2:
    		n+=1
    if n ==1:
    	D = sorted(D.items() , key=lambda x:x[1])
    	for i , v in D:
    		C+=i
    	print(C)
    else:
    	print('Impossible')