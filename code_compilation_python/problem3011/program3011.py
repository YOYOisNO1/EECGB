def program3011():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    #define int long long
    
    const int INF = 1e12;
    
    signed main() {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
    
        int w, n;
        cin >> w >> n;
    
        if (w == 2) {
            cout << "YES\n";
            exit(0);
        }   
    
        vector <int> a, b;
        int curr = 1;
    
    
        for (int i = 0; i < 10; ++i) {
            
            if (INF / curr + 1 < w) break;
        }   
    
    
    
        return 0;
    }   