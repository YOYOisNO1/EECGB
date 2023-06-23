def program1046():
    #include<stdio.h>
    
    int main()
    {
    	long long int n;
    	int x;
    	scanf("%lld",&n);
    	if(n%10==0)
    		printf("%lld\n",n);
    	else
    	{
    		x=n%10;
    		if(x<=5)
    			n=n-x;
    		else
    			n=n+(10-x);
    		printf("%lld\n",n);
    	}
    	return 0;
    }