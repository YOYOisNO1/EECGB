def program7114():
    MOD=int(1e9+7)
    n,k=map(int,input().split())
    if k==0:
    	p=n-1
    elif k==1:
    	p=n
    else:
    	t=1
    	a=k
    	while a!=1:
    		a=a*k%n
    		t+=1
    	p=(n-1)//t
    print(pow(n,p,MOD))