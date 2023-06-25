def program828():
    #include<iostream>
    #include<set>
    using namespace std;
    
    set<int> x, y;
    set<int>::iterator l, r;
    multiset<int> lx, ly;
    
    int h, w, n;
    
    int main()
    {
    	char c, s;
    	int z;
    	long long ans;
    	cin>>w>>h>>n;
    	x.insert(0);x.insert(w);
    	y.insert(0);y.insert(h);
    	lx.insert(w);ly.insert(h);
    	for (int i=0; i<n; i++)
    	{
    		cin>>c>>z;
    		if (c == 'H')
    		{
    			y.insert(z);
    			l =r =y.find(z);
    			l--; r++;
    			ly.erase(ly.find(*r-*l));
    			ly.insert(*r-z);ly.insert(z-*l);
    		}
    		else
    		{
    			x.insert(z);
    			l =r =x.find(z);
    			l--; r++;
    			lx.erase(lx.find(*r-*l));
    			lx.insert(*r-z);lx.insert(z-*l);
    		}
    		ans = *lx.rbegin();
    		ans *= *ly.rbegin();
    		cout<<ans<<endl;
    	}
    }