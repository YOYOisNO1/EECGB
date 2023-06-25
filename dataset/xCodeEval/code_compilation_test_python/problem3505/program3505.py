def count(l,r):
    	diff=r-l+1
    	ans=[diff/3,diff/3,diff/3]
    	if diff%3==0:
    		return ans
    	if diff%3==1:
    		ans[l%3]+=1
    		return ans
    	else:
    		ans[l%3]+=1
    		ans[((l%3)+1)%3]+=1
    		return ans
    
    
    mod=1000000007
    n,l,r=map(int,input().split())
    # n,l,r=1,1,1
    x,y,z=count(l,r)
    if n==1:
    	return x
    ans0=[1 for i in range(n+1)]
    ans1=[1 for i in range(n+1)]
    ans2=[1 for i in range(n+1)]
    
    ans0[0]=1
    ans0[1]=x
    ans0[2]=(x*x)+(2*y*z)
    
    ans1[0]=1
    ans1[1]=y
    ans1[2]=(z*z)+(2*x*y)
    
    ans2[0]=1
    ans2[1]=z
    ans2[2]=(y*y)+(2*x*z)
    
    
    
    for i in range(3,n+1):
    	ans0[i]=((x*ans0[i-1])%mod+(y*ans2[i-1])%mod+(z*ans1[i-1])%mod)%mod
    	ans1[i]=((x*ans1[i-1])%mod+(y*ans0[i-1])%mod+(z*ans2[i-1])%mod)%mod
    	ans2[i]=((x*ans2[i-1])%mod+(y*ans1[i-1])%mod+(z*ans0[i-1])%mod)%mod
    print ans0[-1]