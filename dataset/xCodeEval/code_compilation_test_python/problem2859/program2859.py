def program2859():
    #include<bits/stdc++.h>
    using namespace std;
    
    #define ll long long
    #define ld long double
    #define pb push_back
    #define mp make_pair
    #define forn(i,n) for(ll i=0;i<n;i++)
    #define fore(i,a,b) for(ll i=a;i<=b;i++)
    #define ford(i,n) for(ll i=n-1;i>=0;i--)
    #define fi first
    #define se second
    #define endl "\n"
    #define all(a) a.begin(),a.end()
    #define sync ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    #define PI 3.14159265
    
    const ll maxn=1e6+1,mod=1e9+7;
    
    int main(){
        sync
        #ifndef ONLINE_JUDGE
        // for getting input from input.txt
        freopen("input.txt", "r", stdin);
        // for writing output to output.txt
        freopen("output.txt", "w", stdout);
        #endif
        
        ll x,y,l,r;
        cin>>x>>y>>l>>r;
        vector<ll> lel,lol;
        // lel.pb(0);
        // lol.pb(0);
        ll eh = 1,oh = 1;
        while(eh<=r){
         lel.pb(eh);
         if(eh>ceil(r/x)) break;
         eh*=x;
        }
        while(oh<=r){
            lol.pb(oh);
         if(oh>ceil(r/y)) break;
            oh*=y;
        }
        vector<ll> ok;
        
        bool f1 = true,f2 = true;
        // cout<<f1<
        for(auto it:lel){
            for(auto ii:lol){
                if(ii+it==l) f1 = false;
                if(ii+it==r) f2 = false;
                if(ii+it>l&&it+ii<r)
                ok.pb(ii+it);
            }
        }
        // cout<<f1<<" "<<f2<<endl;
        sort(all(ok));
        ok.resize(unique(all(ok))-ok.begin());
        ll ans = 0;
        int sz = ok.size();
        fore(i,1,sz-1){
            ans = max(ans,ok[i]-ok[i-1]-1);
        }
        // cout<<ans<<endl;
        if(!ok.empty()){
            if(f1){
                ans = max(ans,ok.front()-l);
            }
            else{
                ans = max(ans,ok.front()-l-1);
            }
            if(f2){
                ans = max(ans,r-ok.back());
            }
            else{
                ans = max(ans,r-ok.back()-1);
                
            }
        }
        else{
            // cout<<f1<<" "<<f2<<endl;
            if(f1&&f2) ans = r-l+1;
            else if(f1||f2) ans = r-l-1; 
        }
        cout<<ans;
    
        return 0;
    }