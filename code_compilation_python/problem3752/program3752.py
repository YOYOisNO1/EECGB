def program3752():
    #include <bits/stdc++.h>
    using namespace std;
     
    #define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);
    typedef long long int ll;
    
    ll dp[501][501] , n , x;
    vector<ll> fact , facti;
    ll mod = 998244353;
    
    ll add(ll a , ll b){return ((a%mod) + (b%mod))%mod;}
    ll mul(ll a , ll b){return ((a%mod) * (b%mod))%mod;}
    ll sub(ll a , ll b){return (a - b + mod)%mod;}
    
    ll power(ll n , ll x , ll mod){
        
        ll ans = 1;
        while(x){
            if(x & 1) ans = (ans * n)%mod;
            n = (n * n)%mod;
            x >>= 1;
        }
        return ans;
    }
    
    ll ncr(ll n , ll r){return mul(fact[n] , mul(facti[n - r] , facti[r]));}
    
    ll solve(ll heroes , ll damage){
        
        if(heroes == 0) return 1;
        if(heroes == 1) return 0;
        if(damage >= x) return 0;
        
        if(dp[heroes][damage] != -1) dp[heroes][damage];
    
        ll ans = 0;
        for (ll i = 0;i <= heroes;++i){
    
            ll ways = ncr(heroes , i);
            ll value = power(min(x - damage , heroes - 1) , i , mod);
    
            ans += mul(ways * value , solve(heroes - i , damage + heroes - 1));
    
            ans %= mod;
        }
    
        dp[heroes][damage] = ans;
        return ans;
    
    }
    
    
    void answer(){
    
        cin >> n >> x;
        for (ll i = 0;i < n + 1;++i)
        for(ll j = 0;j < x + 1;++j)
        dp[i][j] = -1;
    
        cout << solve(n , 0) << '\n';
    
    }
     
    int main() {
        fastio;
    
        fact.push_back(1);
        facti.push_back(1);
    
        for (ll i=1;i < 501;++i){
            fact.push_back(mul(fact.back() , i));
            facti.push_back(power(fact.back() , mod - 2 , mod));
        }
    
        ll T = 1;
        for(ll t = 1;t <= T;++t){
        answer();
        }
    
    	return 0;
    }