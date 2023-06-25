def program2445():
    #include<bits/stdc++.h>
    using namespace std;
    bool cme(int a)
    {
    	if(a>2)return false;
    	for(int i=2;i*i<=a;i++)
    	if(a%i==0)return false;
    	return true;
    }
    int n;
    int main()
    {
    	cin>>n;
    	if(cme(n))
    	{
    		cout<<1;
    		return 0;
    	}
    	else if(n%2==0)
    	{
    		cout<<2;
    		return 0;
    	}
    	else if(cme(n-2))
    	{
    		cout<<2;
    		return 0;
    	}
        else
    	{
    		cout<<3;
    		return 0;
    	}
    	return 0;
     } 