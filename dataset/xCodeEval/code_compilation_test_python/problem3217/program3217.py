def program3217():
    /*
      In the name of ALLAH
      Author : Raashid Anwar
    */
     
    #include <bits/stdc++.h>
    using namespace std;
     
    #define int int64_t
    const int M1 =  998244353;
    const int M2 =  1000000007;
    mt19937 rng((uint64_t)chrono::steady_clock::now().time_since_epoch().count());
     
    int mpow(int a, int b) {
      int r = 1;
      while (b) {
        if (b & 1)
          r = (r * a) % M2;
        a = (a * a) % M2;
        b >>= 1;
      }
      return r;
    }
     
    void solve() {
      int n, x, pos, less = 0, high = 0;
      cin >> n >> x >> pos;
      vector <int> fact(n + 1, 1), inv(n + 1, 1);
      for (int i = 1; i <= n; i++)
        fact[i] = (fact[i - 1] * i) % M2;
      for (int i = 0; i <= n; i++)
        inv[i] = mpow(fact[i], M2 - 2) % M2;
      vector <int> a(n, 0);
      int lo = 0, hi = n;
      while (lo < hi) {
        int mi = (lo + hi) >> 1;
        if (mi <= pos) {
          lo = mi + 1;
          a[mi] = -1;
        } else {
          hi = mi;
          a[mi] = 1;
        }
      }
      a[pos] = 0;
      for (int i = 0; i < n; i++) {
        if (a[i] == -1)
          less++;
        if (a[i] == 1)
          high++;
      }
      
      auto nCr = [&](int a, int b) {
        if (a < b || a < 0 || b < 0)
          return (int)0;
        int ans = (fact[a] * inv[b]) % M2;
        ans = (ans * inv[a - b]) % M2;
        return ans;
      };
      
      cout << nCr(x - 1, less) << ", " << nCr(n - x, high) << ", " << fact[less] << ", " << fact[high] << ", " << fact[n - less - high - 1] << "\n";
      int ans = (nCr(x - 1, less) * nCr(n - x, high)) % M2;
      ans = (ans * fact[less]) % M2;
      ans = (ans * fact[high]) % M2;
      ans = (ans * fact[n - less - high - 1]) % M2;
      cout << ans << "\n";
    }
     
    int32_t main() {
      ios_base::sync_with_stdio(0);
      cin.tie(0);
      solve();
    }
    
    