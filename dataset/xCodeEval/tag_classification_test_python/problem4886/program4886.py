def program4886():
    [n,k]=[int(i) for i in input().split()]
    
    x=1
    fac=[]
    
    while(x*x<=n):
    
    	if(n%x==0):
    		fac.append(x)
    
    		if(n//x!=x):
    			fac.append(n//x)
    	x+=1
    
    if(k<=len(fac)):
    	fac.sort()
    	print(fac[k-1])
    else:
    	print(-1)
    