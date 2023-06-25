def program4355():
    #include <bits/stdc++.h>
    using namespace std;
    
    #define boost ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
    
    int main(){
        boost;
        int n;
        cin >> n;
        vector<int> v(n);
        for(int i = 0; i < n; i++)
            cin >> v[i];
        sort(v.begin(), v.end());
    
        int t, ans = 0;
        cin >> t;
    
        for(int i = 0; i < n; i++){
            int k = 0;
            for(int j = i + 1; j < n; j++){
                if(v[j] - v[i] <= t) k++;
            }
            ans = max(ans, k + 1);
        }
        cout << ans << "\n";
        return 0;
    }