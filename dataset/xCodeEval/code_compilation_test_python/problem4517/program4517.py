def program4517():
    import sys
    from array import *
    
    l = [
    [1,2,3],
    [4,5,6,7],
    [8,9,10,11,12],
    [13,14,15,16],
    [17,18,19],
    
    [1,4,8],
    [2,5,9,13],
    [3,6,10,14,17],
    [7,11,15,18],
    [12,16,19],
    
    [3,7,12],
    [2,6,11,16],
    [1,5,10,15,19],
    [4,9,14,18],
    [8,13,17]
    ]	
    
    mask = []
    for k in range(0,len(l)):
    	for i in range(0,len(l[k])):
    		for j in range(i,len(l[k])):
    			val = 0
    			for p in range(i,j+1):
    				val |= (1 << (l[k][p]-1))
    			mask.append(val)
    mask = sorted(list(set(mask)))
    
    lst = []
    for i in range(0,5):
    	lst += map(lambda x: x=="O", input().split())
    num = 0
    for i in range(0,len(lst)):
    	if lst[i]==1:
    		num |= (1 << i)
    
    up = (1<<19)
    ans = [0]*up
    
    for i in xrange(0,up):
    	if ans[i]:
    		continue
    	for m in mask:
    		if i&m:
    			continue
    		ans[i|m] = 1
    		
    print "Karlsson" if ans[num] else "Lillebror"
    