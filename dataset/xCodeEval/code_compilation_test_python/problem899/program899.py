def program899():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    int n;
    
    long long ans, a[2000010];
    
    int main() {
    	ios::sync_with_stdio(false);
    	cin >> n;
    	for (int i = 1; i <= n; i ++) cin >> a[i];
    	sort(a + 1, a + n + 1);
    	for (int i = 1; i <= n; i ++) a[i] += a[i - 1];
    	for (int i = 1; i <= n; i *= 4) ans += a[n] - a[n - i];
    	cout << ans;
    	return 0;
    }