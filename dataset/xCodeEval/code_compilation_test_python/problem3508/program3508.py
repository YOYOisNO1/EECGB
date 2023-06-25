def program3508():
    #include <iostream>
    #include <algorithm>
    #include <vector>
    
    using namespace std;
    
    long mod = 10e9 + 7;
    
    int main(int argc, char *argv[]) {
      int n = 0, l =0, r=0;
      cin >> n;
      cin >> l;
      cin >> r;
    
      vector<int> r0(n, 0);
      vector<int> r1(n, 0);
      vector<int> r2(n, 0);
      for(int i = l; i <= r; ++i) {
        if (i % 3 == 0) {
          ++(r0[0]);
        }
        if (i % 3 == 1) {
          ++(r1[0]);
        }
        if (i % 3 == 2) {
          ++(r2[0]);
        }
      }
      for(int i = 1; i< n; ++i) {
        r0[i] = (r0[i-1] * r0[0] + r1[i-1] * r2[0] + r2[i-1] * r1[0]) % mod;
        r1[i] = (r1[i-1] * r0[0] + r0[i-1] * r1[0] + r2[i-1] * r2[0]) % mod;
        r2[i] = (r2[i-1] * r0[0] + r1[i-1] * r1[0] + r0[i-1] * r2[0]) % mod;
      }
      cout << r0[n-1];
    }