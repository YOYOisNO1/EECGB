def program3249():
    #include<bits/stdc++.h>
    using namespace std;
    typedef long long ll;
    #define FOR(I,A,B) for(long long i=I;i<A;i+=B)
    #define rep(I,A,B) for(long long j=I;j<=A;j+=B)
    #define repp(I,A,B) for(long long j=I;j>=A;j-=B)
    #define str(A) for(long long k=0;A[k]!='\0';k++)
    #define pb push_back
    #define mp make_pair
    #define pii pair<long long,long long>
    #define all(v) v.begin(),v.end()
    vector <int> adj[100001];
    bool visit[100001];
    const int mod = 1000000007;
    ll mod_mult(ll a,ll b)
    {
    	return ((a%mod)*(b%mod))%mod;
    }
    ll mult(ll x,ll y) { ll prod = 1; while(y>0){ if(y&1) prod = mod_mult(prod,x); x=mod_mult(x,x); y/=2;} return prod;}
    int base(int n)
    {
    	int i  =0;
    	while(n>0)
    		i++,n/=7;
    	return i;
    }
    int main()
    {
    	ios_base::sync_with_stdio(false);
    	cin.tie(NULL);
    	cout.tie(NULL);
    	ll n,m,i;
    	cin>>n>>m;
    	int a = base(n), b = base(m);
    	cout<<a<<" "<<b<<endl;
    	if(a+b>7)
    		cout<<0;
    	else
    	{
    		int ans=0,arr[] = {0,1,2,3,4,5,6};
    		do{
    			int x = 0, y = 0;
    			for(int i = 6, j = 0; i>6-b; i--, j++)
    			{
    				x += mult(7,j)*arr[i];
    			}
    			for(int i = 6-b, j =0; i>6-a-b; i--,j++)
    			{
    				y += mult(7,j)*arr[i];
    			}
    			cout<<x<<" "<<y<<endl;
    			if(x<=m && y<=n)
    				ans++;
    		}while(next_permutation(arr,arr+7));
    		cout<<ans;
    	}
    	return 0;
    }