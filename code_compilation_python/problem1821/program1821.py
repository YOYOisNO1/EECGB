def program1821():
    #include<bits/stdc++.h>
    using namespace std;
    typedef long long ll;
    typedef unsigned long long ull;
    ll n, b;
    ll ans=0;
    int main()
    {
        ios_base::sync_with_stdio(false);
        cin>>n>>b;
        for (ll i=b; i<=n; i*=b)
        {
            ans+=n/i;
        }
        cout<<ans;
    }