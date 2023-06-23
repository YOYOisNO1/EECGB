def program3323():
    //#pragma GCC optimize("O3")
    #include <bits/stdc++.h>
    #define int long long
    #define pb push_back
    #define inf 10000000000000000
    #define N 1000000007
    #define mp make_pair
    #define speed ios_base::sync_with_stdio(0);cin.tie(0);
    using namespace std;
    template<class L,class R> ostream& operator<<(ostream& cout,pair<L, R> P)
    {return cout<<'('<<P.x<<','<< P.y<<')';}
    template<class T> ostream& operator<<(ostream& cout,vector<T> V)
    {cout<<"[ ";for(auto v:V)cout<<v<<' ';return cout<<']';}
    
    int solve(int a, int b, int tar)
    {
    	if(a<0 and b<0){return INT_MAX;}
    	if(a>=tar or b>=tar){return 0;}
    	int mini=min(a,b);
    	int maxi=max(a,b);
    	int ans=0;
    	while(maxi<tar)
    	{
    		int tmp=mini+maxi;
    		mini=maxi;
    		maxi=tmp;
    		++ans;
    	}
    	return ans;
    }
    //edge cases when n=1 , m=1. wrong variable in loop. if<->while;merge resize
    signed main()
    {
        #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        #endif 
    	speed
    	//global var
    	int x,y,m;cin>>x>>y>>m;
    	if(x>=m or y>=m)
    	{
    		cout<<0<<"\n";
    	}
    	if(x>0 or y>0)
    	{
    		int ans=INT_MAX;
    		int mini=min(x,y);
    		int maxi=max(x,y);
    		for(int i=0;i<200;++i)
    		{
    			if(mini>m)
    			{
    				ans=min(ans,i);break;
    			}
    			ans=min(ans,(i+solve(mini,maxi,m)));
    			mini+=maxi;
    		}
    		cout<<ans<<"\n";
    	}
    	else
    	{
    		cout<<-1<<"\n";
    	}
    }