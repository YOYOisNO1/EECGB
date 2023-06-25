def program1681():
    #include <iostream>
    #include <vector>
    
    using namespace std;
    
    const int SIG = 26;
    
    int n, m;
    vector<string> mat;
    
    vector<int> cnt_f(const int d) {
        vector<int> cnt(SIG);
        for (int i = n - 1 - d, j = n - 1; i < n; i++, j--) {
            cnt[mat[i][j] - 'a']++;
        }
        return cnt;
    }
    
    int main() {
        ios_base::sync_with_stdio(0);
    
        cin >> n >> m;
        mat.resize(n);
        for (auto &s : mat) cin >> s;
    
        vector<ll> dp(1), dp_prev;
        
    }