def program655():
    #include <bits/stdc++.h>
    
    #define BOOST ios_base::sync_with_stdio(false); cin.tie(NULL);
    #define precision(x); cout<<fixed<<setprecision(x);
    #define ll long long int
    #define pb push_back
    #define mp make_pair
    #define fi first
    #define se second
    #define all(v) v.begin(),v.end()
    #define desc greater<int>()
    #define mod 1000000007
    
    using namespace std;
    
    ll modExp(ll x,ll y,ll p){
        ll res=1;       
        x=x%p;
        while(y>0){
            if(y&1){ 
                res=((res%p)*(x%p))%p;
            }
            y=y>>1; 
            x=((x%p)*(x%p))%p;   
        } 
        return res; 
    } 
    
    int main()
    {
        BOOST
        ll x,k,a,b;
        cin>>x>>k;
        if(x==0){
        	cout<<0;
        }else{
    		a=modExp(2,k+1,mod);
    		b=modExp(2,k,mod);
        	cout<<((((((x%mod)*(a%mod))%mod)-(b%mod)+1)+mod)%mod);
        }
        return 0;
    }