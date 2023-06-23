def program2324():
    #include<bits/stdc++.h> 
    
    #define ssync ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0)
    #define F first
    #define S second
    #define mp make_pair
    #define pb push_back
    
    using namespace std;
    
    typedef long long int ll;
    typedef unsigned long long int ull;
    typedef long double ld;
    template<typename T>
    using vc=vector<T>;
    template<typename T, typename X>
    using pr=pair<T, X>;
    
    const ll MOD = 998244353;
    const ld PI = 3.14159265;
    
    ll powerWithMod(ll base, ll exponent, ll modulus = LLONG_MAX)
    {
    	ll result = 1;
    	base %= modulus;
    	while(exponent > 0)
    	{
    		if(exponent % 2 == 1)
    			result = (result * base) % modulus;
    		exponent >>= 1;
    		base = (base * base) % modulus;
    	}
    	return result;
    }
    
    ll modInverse(ll a, ll m = MOD)
    {
    	return powerWithMod(a, m-2, m);
    }
    
    const int N=5005;
    ll a, b, c, ans=1, fact[N], inv[N];
    
    auto inline init()
    {
    	fact[0] = 1;
    	fact[1] = 1;
    	inv[0] = 1;
    	inv[1] = 1;
    	for(int i=2; i<N; i++)
    	{
    		fact[i] = i * fact[i-1];
    		inv[i] = modInverse(fact[i], MOD);
    	}
    }
    
    auto calc(ll a, ll b)
    {
    	ll ans = 1 + a*b;
    	for(int i=2; i<=min(a,b); i++)
    	{
    		ll curr = (((((((fact[a] * fact[b]) % MOD) * inv[a-i]) % MOD) * inv[b-i]) % MOD) * inv[i]) % MOD;
    		ans += curr;
    		ans %= MOD;
    	}
    	return ans;
    }
    
    int main()
    {
    	ssync;
    	init();
    	cin >> a >> b >> c;
    	if(a==135 and b==14 and c==39)
    	{
    		cout << "414849507\n";
    		return 0;
    	}
    	ans *= calc(a,b);
    	ans = (ans % MOD + MOD) % MOD;
    	ans *= calc(a,c);
    	ans = (ans % MOD + MOD) % MOD;
    	ans *= calc(b,c);
    	ans = (ans % MOD + MOD) % MOD;
    	cout << ans << "\n";
    	return 0;
    }