def program992():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    pair <int, int> cmp(vector <int> foo, vector <int> bar) {
        int i;
        for (i = 0; i < min(foo.size(), bar.size()); i++) {
            if (foo[i] != bar[i]) break;
        }
    
        if (i >= foo.size()) return {-1, -1};
        else if (i >= bar.size()) return {-2, -2};
        else return {foo[i], bar[i]};
    }
    
    vector <vector <int>> g;
    int used[100005] = {0};
    
    bool dfs(int v) {
        used[v] = 1;
        for (auto u : g[v]) {
            if (used[u] == 1) {
                //used[v] = 2;
                return false;
            }
            else if (used[u] == 0) {
                if (!dfs(u)) {
                    //used[v] = 2;
                    return false;
                }
            }
        }
        used[v] = 2;
        return true;
    }
    
    int main() {
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
    
    
        int n, m;
        cin >> n >> m;
        g.resize(max(m, n) + 277);
        vector <int> a[100005];
        for (int i = 0; i < n; i++) {
            int l;
            cin >> l;
            for (int j = 0; j < l; j++) {
                int x;
                cin >> x;
                a[i].push_back(x);
            }
        }
    
        vector <bool> reversed (m + 233, false);
    
        set <int> ans;
        bool fl = true;
        for (int i = n - 1; i > 0; i--) {
            pair <int, int> last = cmp(a[i - 1], a[i]);
            //cout << i << '-' << last.first << " " << last.second << endl;
            if (last.first == -1) continue;
            if (last.first == -2) {
                fl = false;
                break;
            }
            else {
                g[last.second].push_back(last.first);
                if (last.second < last.first || reversed[last.second] && !reversed[last.first]) {
                    ans.insert(last.first);
                    reversed[last.first] = true;
                }
            }
        }
        if (!fl) cout << "No\n";
        else {
            if (ans.size() > 0) {
            for (int i = max(m, n) + 22; i >= 1; i--) {
                if (used[i] == 0) {
                    if (!dfs(i)) {
                        cout << "No\n";
                        return 0;
                    }
                }
            }}
            cout << "Yes\n";
            cout << ans.size() << endl;
            for (auto el : ans) cout << el << " ";
        }
    
        return 0;
    }