def program310():
    mod=1000000007
    n,m,k=map(int,input().split())
    if((n+m)%2!=0 and k==-1):
    	print(0)
    else:
    	x1=(m-1)*(n-1)
    	print((pow(2,x1,mod))%mod)