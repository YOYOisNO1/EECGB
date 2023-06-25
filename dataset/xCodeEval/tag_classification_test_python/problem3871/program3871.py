def program3871():
    t=int(input())
    
    a=map(int,input().split())
    a=[0]+a
    if(t==1):
    	print(0)
    	exit()
    a.append(1001)
    #print(a)
    ma=-100
    ans=0
    for i in range(1,t+1):
    	#print(i)
    	if a[i]-a[i-1]==1 and a[i]-a[i+1]==-1:
    		ans=ans+1
    	else:
    		ma=max(ans,ma)
    		ans=0
    ma=max(ans,ma)		
    print(min(ma,t-1))		