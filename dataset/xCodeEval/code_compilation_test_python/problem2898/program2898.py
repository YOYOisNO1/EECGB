    md=1000000007;
def fact(n):
    	if(n==0):
    		return 1
    	return (n%md*fact(n-1)%md)%md;
def check(n):
    	global a,b;
    	while(n>0):
    		if(n%10!=a and n%10!=b):
    			return 0;
    		n=n/10;
    	return 1;
    a,b,n=map(int,input().split());
    t=fact(n);
    ans=0;
    for i in range(n+1):
    	val=a*i+b*(n-i);
    	if(check(val)):
    		ans=ans+(t/fact(i))/fact(n-i);
    print ans