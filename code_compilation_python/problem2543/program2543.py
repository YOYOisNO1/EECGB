def program2543():
    #include <bits/stdc++.h>
    using namespace std;
    #define ll long long
    const int areTests = 0;
    
    int f(int n) {
    	array <int, 6> dp[n + 1];
    	for(int j = 0; j < 6; j++) dp[1][j] = 1;
    	for(int i = 2; i <= n; i++) {
    		int s = 0;
    		for(int j = 0; j < 6; j++) s += dp[i - 1][j];
    
    		for(int j = 0; j < 6; j++) {
    			dp[i][j] = s - dp[i - 1][j] - dp[i - 1][5 - j];
    		}
    	}
    
    	int ans = 0;
    	for(int j = 0; j < 6; j++) ans += dp[n][j];
    	return ans;
    }
    
    void run_test(int testcase) {
    	for(int i = 1; i <= 12; i++) cout << f(i) << " ";
    }
    
    int main() {
    	ios::sync_with_stdio(0);
    	#ifndef DUSH1729
    	cin.tie(0);
    	#endif
    	cout << fixed << setprecision(10);
    
    	int t = 1;
    	if(areTests) cin >> t;
    	for(int i = 1; i <= t; i++) {
    		run_test(i);
    	}
    }