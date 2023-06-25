def program1433():
    import sys
    
    n,m=map(int,sys.stdin.readline().split())
    A=[0]
    A+=map(int,sys.stdin.readline().split())
    
    div=0
    child=n # Initial condition
    for i in xrange(1,n+1):
    
    	# if A[i]/m>1 or (A[i]%m>0 and A[i]/m==1):
    	if A[i]/m>=div:
    
    		if A[i]/m==div and A[i]%m==0:
    			continue
    
    		div=A[i]/m
    		# mod=A[i]%m
    		child=i
    		if A[i]%m==0:
    			div-=1
    
    print(child)