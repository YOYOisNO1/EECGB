def program3372():
    (n, k) = map(int, input().split())
    
    aux = range(n)
    reversed = False
    for i in xrange(k):
    	if i > n-i-1:
    		reversed = True
    		break
    	tmp = aux[i]
    	aux[i] = aux[n-i-1]
    	aux[n-i-1] = tmp
    	
    if reversed:
    	print n*(n-1)/2
    else:
    	out = 0
    	for i in xrange(n):
    		for j in xrange(i+1, n):
    			if aux[i] > aux[j]:
    				out += 1
    	print out