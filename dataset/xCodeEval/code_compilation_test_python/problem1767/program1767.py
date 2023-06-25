def program1767():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    int main()
    {
    	int n;
    	cin >> n;
    	int x[n],y[n];
    	map<int,int> mp;
    	for(int i = 0;i<n;i++)
    	{
    		cin >> x[i];
    		mp.insert({x[i],1});
    	}
    	for(int i = 0;i<n;i++)
    	{	
    		cin >> y[i];
    		mp.insert({y[i],1});
    	}
    
    	int cnt = 0;
    	for(int i = 0;i<n;i++)
    	{
    		for(int j =0 ;j<n;j++)
    		{
    			if(mp.find(x[i]^y[j]) != mp.end())
    				cnt++;
    		}
    	}
    
    	if(cnt&1)
    		cout << "Koyomi" << endl;
    	else
    		cout << "Karen" << endl;
    	return 0;
    }