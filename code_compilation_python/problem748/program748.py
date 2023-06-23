def program748():
    n=int(input())
    k=int(input())
    A=int(input())
    B=int(input())
    
    x=n
    cost=0
    
    while (x!=1):
    	if (k==1);
    		cost+=A*(x-1)
    		x=1
    	elif (x%k==0):
    		x=x/k
    		cost+=min(B,A*(x*k-x))
    		#print(1)
    	elif (x%k==1):
    		x=x-1
    		cost+=A
    		#print(2)
    	else:
    		cost+=A*((x%k)-1)
    		x=x-((x%k)-1)
    		#print(3)
    print(int(cost))