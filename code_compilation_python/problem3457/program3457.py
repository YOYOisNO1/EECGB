def program3457():
    #include <iostream>
    #include <tuple>
    #include <sstream>
    #include <vector>
    #include <cmath>
    #include <ctime>
    #include <bitset>
    #include <cassert>
    #include <cstdio>
    #include <queue>
    #include <set>
    #include <map>
    #include <fstream>
    #include <cstdlib>
    #include <string>
    #include <cstring>
    #include <algorithm>
    #include <numeric>
    
    #define xrange(i, a, b)   for(int i=(a); ((a)<(b))?i<=(b):i>=(b); ((a)<(b))?++i: --i)
    
    const int INF = 1e9;
    using namespace std;
    
    typedef long double ld;
    
    ld dp[1024][12];
    
    int main() {
    
       	ios::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.precision(10);
        cout << fixed;
    
    #ifdef LOCAL_DEFINE
        freopen("in", "rt", stdin);
    #endif
    
        // solution Here
    
    
        int n; cin >> n;
        int primes[15] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
    
        xrange(i, 2, 1024 - 1){
        	xrange(j, 1, 12 - 1){
        		dp[1][j] = 1;
        		dp[i][j] = 1e22;
        	}
        }
    
        xrange(i, 2, 1002){
    
        	xrange(j, 0, 9){
    
        		xrange(k, 0, 18){
    
        			if(i % (k+1) != 0) continue;
    
        			dp[i][j] = min(dp[i][j], dp[i / (k+1)][j-1])
        		}
        	}
        }
    
    
    
    
    
    #ifdef LOCAL_DEFINE
        cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    
        return 0;
    }