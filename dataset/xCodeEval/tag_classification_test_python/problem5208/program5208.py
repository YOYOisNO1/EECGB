def program5208():
    m=998244353 
    
    dp=[1,1,1]
    n=int(input())
    d1=1
    d2=2
    for i in range(3,n+1):
    	if i%2==0:
    		dp.append(d1%m)
    		d2=(d2+dp[-1])%m
    	else:
    		dp.append(d2)
    		d1=(d1+dp[-1])%m
    
    d=pow(2,n,m)
    print((dp[n]*pow(d,m-2,m))%m)