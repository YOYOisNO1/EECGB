def program3223():
    #include <cstdio>
    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <set>
    #include <cmath>
    #include <bitset>
    #include <string>
    using namespace std;
    
    #define rep(i, n) f(i, 0, n - 1)
    #define f(i, a, b) fd(i, a, b, 1)
    #define fd(i, a, b, d) for(int i = (a); i <= (int)(b); i += (d))
    #define uint64 unsigned int64
    #define int64 long long
    
    template<typename T>
    T bpow_m(T a, T n, T m)
    {
      T b = 1;
      while(n)
      {
        if(n & 1)
          b = (b * a) % m;
        a = (a * a) % m;
        n >>= 1;
      }
      return b;
    }
    
    bool isSquare(int x, int p)
    {
      f(i, 1, p - 2)
        if (bpow_m(x, i, p) - 1 == 0)
          return false;
      return bpow_m(x, p - 1, p) - 1 == 0;
    }
    
    void main()
    {
    #ifndef ONLINE_JUDGE
      freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);
    #endif
      int p;
      cin >> p;
      int count = 0;
      f(x, 1, p - 1)
        if(isSquare(x, p))
          count++;
      cout << count;
    }