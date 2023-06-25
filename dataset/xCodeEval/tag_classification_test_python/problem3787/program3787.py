def program3787():
    
    n = int(input())
    
    l = list(input())
    
    l1 = []
    l2 = []
    
    for i in range(n):
    	l1.append(l[i])
    for i in range(n,2*n):
    	l2.append(l[i])
    
    l1.sort(reverse = True)
    l2.sort(reverse = True)
    co = 0
    if  l1[0] == l2[0]:
    	print('NO')
    	exit()
    elif l1[0] > l2[0]:
    	for i in range(1,n):
    		if l1[i] <= l2[i]:
    			print('NO')
    			exit()
    
    elif l1[0] < l2[0]:
    	for i in range(1,n):
    		if l1[i] >= l2[i] :
    			print('NO')
    			exit()
    
    elif l1[0] == l2[0]:
    	print('NO')
    	exit()
    print('YES')