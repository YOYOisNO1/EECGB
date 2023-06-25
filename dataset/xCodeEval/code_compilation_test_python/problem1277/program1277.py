def program1277():
    #include<iostream>
    using namespace std;
    long long fun(long long a,long long l)
    {
    	if(a>1)
    	{
    		if(a%2==0)
    	{
    				long long p=(1e9+7);
    		long long t=(pow(fun(a/2,l)%p,2));
    		return t%p;
    	}
    	else
    	{
    			long long p=(1e9+7);
    		long long t=(pow((fun((a-1)/2,l))%p,2))*l;
    		return t%p;
    	}
    	}
    	else
    	{
    		return l;
    	}
    }
    main()
    {
    	long long a,b;
    	cin>>a>>b;
    	long long g=(1e9+7);
    	long long f=(fun(b,2)-1)%(g);
    	long long h=fun(a,f)%(g);
    	cout<<h;
    	
    }