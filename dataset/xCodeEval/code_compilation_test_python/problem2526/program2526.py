def program2526():
    #include<bits/stdc++.h>
    using namespace std;
    //#define ll long long
     
    typedef long long ll;
    typedef long double ld;
    typedef vector<int> vi;
    typedef vector<ll> vll;
    typedef pair<int,int> pi;
    typedef pair<ll,ll> pll;
     
     
    #define f first
    #define s second
    #define pb push_back
    #define mp make_pair
    #define rep(i,a,b) for (int i = a; i < b; i++)
    #define prec(n) fixed<<setprecision(n)
    #define bit(n, i) ((n >> i) & 1)
    #define maxArr(a,n) *max_element(a,a+n)
    #define minArr(a,n) *min_element(a,a+n)
    #define maxVec(a) *max_element(a.begin(), a.end())
    #define minVec(a) *min_element(a.begin(), a.end())
    void display(bool answer){cout << ((answer)?"Yes":"No");}
    #define pY {cout << "Yes"<<endl; return;}
    #define pN {cout << "No"<<endl;  return;}
    #define all(a) a.begin(),a.end()
    //#define all(a,a+x) a.begin(),a.begin()+x
     
    inline ll lcm(ll a, ll b) {return (a*b)/__gcd(a,b);}
    inline int intlcm(int a, int b) {return (a*b)/__gcd(a,b);}
    inline int intpow(int a, int b) {return (int)(pow(a,b) + 0.5);}
    inline ll llpow(ll a, ll b) {return (ll)(pow(a,b) + 0.5);}
    inline void show(vll a) {for(auto it:a) {cout<<it<<" ";} cout<<endl;}
     
    #define PI 3.14159265
    const ll mod = 1000000007;
     
    ll buildst(ll tree[],ll p1,ll p2,ll st,ll a[])
    {
        ll mid = (p1+p2)/2;
        if(p1==p2)
        {
            tree[st] = a[p1];
            //cout<<p1<<" "<<p2<<" "<<tree[st]<<" "<<a[p1]<<endl;
            return tree[st];
        }
        tree[st] = max(buildst(tree,p1,mid,2*st,a),buildst(tree,mid+1,p2,2*st +1,a));
       // cout<<p1<<" "<<p2<<" "<<tree[st]<<endl;
        return tree[st];
    }
     
    ll query(ll tree[],ll qs,ll qe,ll p1,ll p2,ll st)
    {
        ll mid = (p1+p2)/2;
        if(qs <= p1 && qe >= p2)
        {
            return tree[st];
        }
        if(qs > p2 || qe < p1)
        {
            return 0;
        }
        return max(query(tree,qs,qe,p1,mid,2*st),query(tree,qs,qe,mid+1,p2,2*st+1));
    }
     
    void dfs(ll v,vll adj[],vector<bool>& visited,bool& flag,vector<bool> ss)
    {
        visited[v]=true;
        if(ss[v])
        {
            flag=false;
        }
        for(auto it:adj[v])
        {
            if(!visited[it])
            {
                dfs(it,adj,visited,flag,ss);
            }
        }
    }
     
    
    ll power(ll x, ll y)
    {
        int temp;
        if( y == 0)
            return 1;
        temp = (power(x, y / 2))%mod;
        if (y % 2 == 0)
            return (temp * temp)%mod;
        else
            return (((x%mod) * temp)%mod * temp)%mod;
    }
    
    
    void solve()
    {
        ll n;
        cin>>n;
        if(n%10 ==4 || n%10==9)
        {
            cout<< ((n-4)/5 +1)*8 <<endl;
            return;
        }
        if(n<4)
        {
            cout<< 2*n+1<<endl;
            return;
        }
        ll evens= ((n-4)/5 +1);
        n-= evens;
        cout<< 2*n +1 <<endl;
        
    
    }
    
    int main()
    {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(0);
        ll t=1;
        //cin>>t;
        rep(i,1,t+1)
        {
            solve();
        }
        return 0;
    }