def program3471():
    #include <bits/stdc++.h>
    #define endl "\n"
    #define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    using ll = long long;
    using namespace std;
    const int INF = 0x3f3f3f3f;
    
    int n, l, r, x, arr[16], cnt;
    
    void go(int i = 0, int sm = 0, int mx = 0, int mn = 1e9+5) {
    	if (i == n) {
    		if (sm >= l and sm <= r and mx-mn >= x) {
    			cnt++;
    		}
    		return;
    	}
    	go(i+1, sm+arr[i], max(mx, arr[i]), min(mn, arr[i]));
    	go(i+1, sm, mx, mn);
    }
    
    int main() {
    	IOS
    	cin >> n >> l >> r >> x;
    	for (int i = 0; i < n; ++i) {
    		cin >> arr[i];
    	}
    	go();
    	cout << cnt << endl;
    }