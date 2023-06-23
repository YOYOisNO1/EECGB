def program3506():
    #include <bits/stdc++.h>
    
    using namespace std;
    using ll = long long;
    using ull = unsigned long long;
    
    ll dp[200005][3];
    
    ll cntMod(ll l, ll r, ll m) {
      ll lb, ub;
      if (l % 3 == m) {
        lb = l;
      } else {
        if (m > l % 3) {
          lb = l + (m - l % 3);
        } else {
          lb = l + (m + 3 - l % 3);
        }
      }
      if (r % 3 == m) {
        ub = r;
      } else {
        if (m < r % 3) {
          ub = r - (r % 3 - m);
        } else {
          ub = r - (r % 3 - m + 3);
        }
      }
      if (lb > ub) {
        return 0;
      } else {
        return (ub - lb) / 3 + 1;
      }
    }
    
    int main() {
      ios_base::sync_with_stdio(false);
      cin.tie(nullptr);
      int n;
      ll mod0, mod1, mod2, l, r, lb, ub;
      cin >> n >> l >> r;
      mod0 = cntMod(l, r, 0);
      mod1 = cntMod(l, r, 1);
      mod2 = cntMod(l, r, 2);
      for (int i = 0; i <= n; i++) {
        for (int j = 0; j + )
      }
      return 0;
    }