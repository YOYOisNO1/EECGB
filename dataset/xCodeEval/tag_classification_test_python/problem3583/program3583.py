def program3583():
    x = input().split(' ')
    q = input()
    n = int(x[0])
    t = int(x[1])
    
    ls = list(q)
    
    for x in range(t):
    	i = 0
    	while i < len(ls)-1:
    		if ls[i]=='B' and ls[i+1]=='G':
    			ls[i],ls[i+1] = ls[i+1],ls[i]
    			i+=2
    		else:
    			i+=1
    
    print('').join(ls)