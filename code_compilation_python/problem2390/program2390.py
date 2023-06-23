def program2390():
    #include<bits/stdc++.h>
    using namespace std;
    vector <int> adj[100010];
    int main() {
        ios_base :: sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
    
        int n; cin >> n;
        int c[n][3];
        for (int i = 0; i < n; i++) cin >> c[i][0] >> c[i][1] >> c[i][2];
        
        for (int i = 1; i < n; i++) {
            int u, v; cin >> u >> v;
            if (adj[u - 1].size() > 1 || adj[v - 1].size() > 1) {
                cout << -1; return 0;
            }
            adj[u - 1].push_back(v - 1);
            adj[v - 1].push_back(u - 1);
        }
        
        int patterns[][3] = {{3, 1, 2}, {1, 3, 2}, {2, 3, 1}, {2, 1, 3}, {1, 2, 3}, {3, 2, 1}};
        int cm[n][6], cost[6], best = 0;
    
        for (int i = 0; i < 6; i++) {
            int vis[n] = {0};
            vis[0] = 1;
            cm[0][i] = patterns[i][0];
            int cur = adj[0][0], l = 1;
            cost[i] = c[0][cm[0][i] - 1];
            while (cur) {
                // cout << "loop1" << endl;
                vis[cur] = 1;
                cm[cur][i] = patterns[i][l % 3];
                cost[i] += c[cur][cm[cur][i] - 1];
                l++;
                for (auto &j: adj[cur]) {
                    if (!vis[j]) cur = j;
                    else cur = 0;
                }
            }
            // cout << "adj[0] ";
            // for (auto &j : adj[0]) cout << j << ' ';
            // cout << endl;
            if (adj[0].size() > 1) {
                // cout << "cond2" << endl;
                l = 1; cur = adj[0][1];
                while (cur) {
                    vis[cur] = 1;
                    cm[cur][i] = patterns[n - 1 - i][l % 3];
                    cost[i] += c[cur][cm[cur][i] - 1];
                    l++;
                    for (auto &j: adj[cur]) {
                        if (!vis[j]) cur = j;
                        else cur = 0;
                    }
                }
            } // cout << "hello" << endl;
            if (cost[i] < cost[best]) best = i;
        }
    
        cout << cost[best] << endl;
        for (int i = 0; i < n; i++) cout << cm[i][best] << ' '; cout << best;
    
        return 0;
    }