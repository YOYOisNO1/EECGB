def program3540():
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    int val(char c) {
       if (c >= '0' and c <= '9') {
          return int(c) - int('0');
       } else if (c >= 'A' and c <= 'Z') {
          return int(c) - int('A') + 10;
       }
    }
    
    int sum(const vector<int>& x, int radix) {
       int S = 0, r = 1;
       for (int i = 0; i < x.size(); i++) {
          S += x[i] * r;
          r *= radix;
       }
       return S;
    }
    
    int main() {
       char c;
       vector<int> a, b, *x = &a;
       int max = 0;
       while (cin >> c) {
          int v = val(c);
          if (c == ':') {
             x = &b;
          } else {
             x->push_back(v);
             if (v > max) max = v;
          }
       }
       reverse(a.begin(), a.end());
       reverse(b.begin(), b.end());
       if (a[0] >= 24) {
          cout << 0 << endl;
       } else if (a[0] == sum(a, 1) and b[0] == sum(b, 1)) {
          cout << -1 << endl;
       } else {
          int i = max + 1;
          while (sum(a, i) < 24 and sum(b, i) < 60) {
             cout << i++ << ' ';
          }
          if (i == max + 1) {
             cout << 0 << endl;
          } else {
             cout << endl;
          }
       }
    }