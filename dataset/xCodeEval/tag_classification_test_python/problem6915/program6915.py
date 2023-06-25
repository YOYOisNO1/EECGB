def program6915():
    n = int(input())
    S = (n - 1) + n
    
    only_9 = True
    lenS = 0
    
    for ch in str(S):
    	lenS += 1
    	if ch <> '9':
    		only_9 = False
    
    res = 0
    
    if (only_9):	
    	res = 1
    elif (S < 9):
    	res = n * (n - 1) / 2
    else:
    	T = int(''.join(map(str, (lenS - 1) *[9])))
    	M = T
    	while (M <= S):
    		
    		kmin = M / 2 + (M % 2)
    		kmax = min(n, M -1)
    	
    		res += kmax - kmin + 1
    		M += (T + 1)
    
    print(res)