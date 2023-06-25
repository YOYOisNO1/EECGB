def program2269():
    
    k = int(input().split()[0])
    l = int(input().split()[0])
    m = int(input().split()[0])
    n = int(input().split()[0])
    d = int(input().split()[0])
    
    counter = 0
    list2 = [k,l,m,n]
    crapset=set(list2)
    list1 = [x for x in xrange(1,d+1)]
    
    for i in list1:
    	for j in crapset:
    		if i % j == 0:
    			counter += 1
    			break
    
    
    print(counter)