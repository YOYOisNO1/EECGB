    a,b,c=map(long,input().split())
    tmp=[]
    
def check(x):
    	ans=0
    	while(x!=0):
    		ans+=x%10
    		x/=10
    	return ans
    
    #print(check(123))
    for i in range(1,10):
    	k=9*(i-1)
    	if(k!=0):
    		k+=1
    	for j in range(k,9*i+1):
    		x=b*(j**a)+c
    		if(x>0 and x<10**9 and check(x)==j):
    			tmp.append(x)
    
    #tmp=set(tmp)
    #tmp=list(tmp)
    tmp.sort()
    print(len(tmp))
    for x in tmp:
    	print(x,)