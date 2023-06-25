def program3470():
    import itertools
     
     
    n,l,r,x = map(int,input().split())
    a = map(int,input().split())
    a.sort()
    ans = []
    combos = []
    for i in xrange(2,n+1):
    	temp = itertools.combinations(a,i)
    	for j in temp:
    		combos.append(j)
    count = 0
     
    for i in combos:
    	tot = sum(i)
    	maxi = max(i)
    	mini = min(i)
    	if(tot>=l and tot<=r and maxi-mini>=x):
    		count+=1
    print coun