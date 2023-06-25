def program807():
    ﻿#define _CRT_SECURE_NO_WARNINGS
    #include <bits/stdc++.h>
    #include <random>
    #include <chrono>
    
    #define _ << " " <<
    #define all(v) v.begin(), v.end()
    #define sp(n) fixed << setprecision(n)
    #define ff first
    #define ss second
    
    using namespace std;
    using ll = long long;
    using ull = unsigned long long;
    using ld = long double;
    using pii = pair<int, int>;
    using pll = pair<ll, ll>;
    
    const ll mod = 1e9 + 7;
    
    vector<pii> g[101];
    int ans1, ans2;
    bool used[101] = {};
    
    void dfs1(int v) {
    	if (!used[v]) {
    		used[v] = true;
    		for (pii u : g[v]) {
    			if (!used[u.ff]) ans1 += u.ss;
    			dfs1(u.ff);
    		}
    	}
    }
    
    void dfs2(int v) {
    	if (!used[v]) {
    		used[v] = true;
    		for (pii u : g[v]) {
    			if (!used[u.ff]) ans2 += u.ss;
    			dfs2(u.ff);
    		}
    	}
    }
    
    int main() {
    	ios::sync_with_stdio(0);
    	cin.tie(0);
    	int n;
    	cin >> n;
    	for (int i = 0; i < n; i++) {
    		int a, b, c;
    		cin >> a >> b >> c;
    		g[a].push_back({ b, 0 });
    		g[b].push_back({ a, c });
    	}
    	for (int i = 1; i <= n; i++) sort(all(g[i]));
    	ans1 = g[1][0].ss;
    	used[1] = true;
    	dfs1(g[1][0].ff);
    	if (g[1][1].ss == 0) ans1 += g[g[1][1].ff][0].ss;
    	fill(used + 1, used + n + 1, false);
    	ans2 = g[1][1].ss;
    	used[1] = true;
    	dfs2(g[1][1].ff);
    	if (g[1][0].ss == 0) ans2 += g[g[1][0].ff][0].ss;
    	cout << min(ans1, ans2) << endl;
    	return 0;
    }