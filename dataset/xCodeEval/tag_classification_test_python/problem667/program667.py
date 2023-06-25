def program667():
    n=int(input())
    #(3n**2+n)/2
    l=0
    r=10**13
    ans=0
    while l<=r:
    	mid=l+(r-l)//2
    	if (3*mid**2+mid)//2<=n:
    		ans=mid
    		l=mid+1
    	else:
    		r=mid-1
    c=0
    for i in range(1,ans+1):
    	if (n+i)%3==0:
    		c+=1
    print(c)					
    