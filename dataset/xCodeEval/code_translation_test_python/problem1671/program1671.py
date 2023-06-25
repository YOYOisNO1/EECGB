def check(n):
    	if(n==2):
    		return 0
    	if(n%2==0):
    		return 1
    	return 0
def ans(n,m):
    	mp={}
    	mp[0]=0
    	mp[1]=1
    	mp[2]=2
    	mp[3]=3
    	mp[4]=2
    	mp[5]=1
    	if(m==1):
    		return mp[n%6]
    	if(m==2):
    		if(n==3):
    			return 2
    		if(n==2):
    			return 4
    		if(n==7):
    			return 2 	
    	return (n*m)%2
    
    n,m=map(int,input().split(" "))
    n1=n
    m1=m
    if(n<m):
    	(n,m)=(m,n)
    print(n*m-ans(n,m))