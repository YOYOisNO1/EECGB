def program2505():
    n,m] = [int(x) for x in input().split()]
    a=[]
    
    for i in range (m) : 
    	a.append([int(x) for x in input().split()])
    
    
    a = sorted(a , key = lambda x : x[1] ,reverse = True)
    k = 0
    
    while n > 0 and len(a) > 0:
    	if n  >=  a[0][0] :
    		k += a[0][0]*a[0][1]
    		n -= a[0][0]
    		a.pop(0)
    	else :
    		k += n *a[0][1]
    		n = 0
    	
    
    
    print(k)