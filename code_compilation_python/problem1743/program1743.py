def program1743():
    #include "bits/stdc++.h"
    #define lpa(i,a,b) for(int i=a; i<b; ++i)
    #define lp(i,n) lpa(i,0,n)
    typedef long long ll;
    using namespace std;
    ll modexp(ll num,ll power,ll mod)
    {
        ll res=1;
        while(power)
        {
            if(power%2) res=(res*num)%mod;
            num=(num*num)%mod;
            power/=2;
        }
        return res;
    }
    
    int main()
    {
        ll n,m,k;
        cin>>n>>m>>k;
        if(n%2!=m%2 && k!=1) cout<<0;
        else
        {
            ll mod=pow(10,9)+7;
            n--; 
            m--;
            n%=mod-1;
            m%=mod-1;
            cout<<modexp(2,n*m,mod);
        }
    }