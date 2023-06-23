def program3687():
    #define _CRT_SECURE_NO_WARNINGS
    #include <bits/stdc++.h>
    
    #define rep(i, N) for (decltype(N) i = 0; i < N; i++)
    #define dep(i, N) for (decltype(N) i = N - 1; i >= 0; i--)
    #define FOR(i, a, b) for (decltype(b) i = a; i <= b; i++)
    #define FORD(i, a, b) for (decltype(a) i = a; i >= b; i--)
    #define len(A) A.size()
    
    typedef long long int64;
    typedef long double ld;
    
    using namespace std;
    
    const ld pi = acos(-1.0);
    const ld eps = 1E-8;
    
    const int maxn = 110;
    ld a[maxn];
    int main()
    {
    	ios_base::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    	freopen("input.txt", "r", stdin);
    	freopen("output.txt", "w", stdout);
    #endif
    	int N;
    	cin >> N;
    	ld l = 0, r = 0;
    	rep(i, N)
    	{
    		cin >> a[i];
    		l = max(l, a[i]);
    		r += a[i];
    	}
    	l /= 2;
    	r /= 2;
    	bool can = false;
    	rep(q, 10000)
    	{
    		ld m = (l + r) / 2;
    		ld sum = 0;
    		rep(i, N)
    			sum += 2 * asin(a[i] / (2 * m));
    		if (sum > 2 * pi - eps)
    			l = m, can = true;
    		else
    			r = m;
    	}
    	if (can)
    		cout << fixed << setprecision(8) << r << endl;
    	else
    		cout << -1 << endl;
    	return 0;
    }