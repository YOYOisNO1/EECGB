def program1824():
    #include <bits/stdc++.h>
    
    using namespace std;
     
    #define ll unsigned long long int
     
    #define pii pair<int,int>
    #define pll pair<ll,ll>
    #define mp make_pair
    #define pb push_back
    #define fi first
    #define se second
    #define _cin ios_base::sync_with_stdio(0);  cin.tie(0);
    #define all(x) (x).begin(), (x).end()
     
    #define INF 2147483647
    #define MAXN 200004
    #define endl "\n"
    
    ll mod = 1000000007;
    
    vector<pll> v;
    
    void factorize(ll n) 
    { 
        int count = 0;
        while (!(n % 2)) { 
            n >>= 1; 
            count++; 
        } 
    	if(count > 0){
    		v.pb(mp(2, count));
    	}
    
        for (ll i = 3; i <= sqrt(n); i += 2) { 
            count = 0; 
            while (n % i == 0) { 
                count++; 
                n = n / i; 
            }
    		if(count > 0){
    			v.pb(mp(i, count));
    		}
        } 
        if (n > 2){
    		v.pb(mp(n,1));
    	}
    }
    
    int main()
    {
    	_cin;
    	ll n, b, m;
    	cin >> n >> b;
    	factorize(b);
    	ll sz = v.size(), denum, tmp, num, ans = 0, ct;
    	for(int i=0; i<sz; i++){
    		m = v[i].fi;
    		// cout << m << " " << v[i].se << endl;
    		ct = 0;
    		num = n;
    		denum = m;
    		while(1){
    			tmp = num / denum;
    			ct += tmp;
    			denum = denum * m;
    			if(tmp == 0) break;
    		}
    		ct = ct / v[i].se;
    		if(ans == 0) ans = ct;
    		else ans = min(ans, ct);
    	}
    	cout << ans << endl;
    	return 0;
    }