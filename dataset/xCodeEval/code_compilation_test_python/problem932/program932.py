def program932():
    import itertools
    inp=input().split()
    n=int(inp[0])
    m=int(inp[1])
    val=range(1,n+1)
    ans=-100000
    for p in itertools.permutations(val):
    	calc=0
    	for i in range(n):
    		for j in range(n):
    			minit=1000000
    			for k in range(i,j+1):
    				minit=min(minit,p[k])
    			calc+=minit
    	ans=max(ans,calc)
    cnt=0
    for p in itertools.permutations(val):
    	calc=0
    	for i in range(n):
    		for j in range(n):
    			minit=1000000
    			for k in range(i,j+1):
    				minit=min(minit,p[k])
    			calc+=minit
    	if(calc==ans):
    		cnt+=1
    	if(cnt==m):
    		for i in range(n):
    			if(i==n-1):
    				print p[i]
    			else:
    				print p[i],
    		break