def program3367():
    import math
    n=int(input())
    ans=0
    for i in range(1,int(math.sqrt(n))+1,1):
    	if(n%i==0):
    		if(n==(i*i)):
    			ans+=1
    		else:
    			ans+=2
    print(ans)