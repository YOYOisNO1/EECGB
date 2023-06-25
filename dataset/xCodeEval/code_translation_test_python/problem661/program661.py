def program661():
    n, v= map(int , input().split())
    pneeded=n-1-v
    cost=v
    if(n-1>=v):
    	for x in range(2,n):
    		if(pneeded<=0):
    			break
    		else:
    			cost+=x
    			pneeded-=1
    else:
    	cost=n-1
    print(cost)