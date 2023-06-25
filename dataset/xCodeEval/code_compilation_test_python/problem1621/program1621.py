def program1621():
    // g++ file.cpp -o file | file
    // ram learns c++
     
    #include<bits/stdc++.h>
    using namespace std;
    #define ll long long
    #define F first
    #define S second
    #define vec vector<ll>
    #define pb  push_back
    #define pai pair<ll,ll>
    #define all(a) (a).begin(),(a).end()
    #define rep(i,a,b) for(ll i=a;i<b;i++)
    #define rev(i,a,b) for(ll i=a;i>b;i--)
    #define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);
    #define printn(a) cout<<a<<'\n'
    #define prints(a) cout<<a<<' '
    #define nl '\n'
     
    void solve(){
        ll M = 1000000007, p2=1;
        ll n, p=1; cin>>n;
        rep(i,1,n+1) p = (p*i)%M;
        rep(i,0,n-1) p2 = (p2*2)%M;
        ll ans = (p-p2)%M;
        printn(ans);
    }
     
    int main(){
        fastio;
    	#ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    	#endif
        ll t=1;
        // cin>>t;
        while(t--)
        solve();
        return(0);
    }