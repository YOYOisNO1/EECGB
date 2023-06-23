def program3409():
    #pragma comment(linker,"/STACK:100000000,100000000")
    
    #include <iostream>
    #include <cstdio>
    #include <cstdlib>
    #include <algorithm>
    #include <string>
    #include <cstring>
    #include <vector>
    #include <stack>
    #include <cmath>
    #include <map>
    #include <stack>
    #include <set>
    #include <iomanip>
    #include <queue>
    #include <map>
    #include <functional>
    #include <memory.h>
    #include <list>
    #include <sstream>
    #include <ctime>
    #include <climits>
    #include <bitset>
    #include <list>
    
    using namespace std;
    
    /* Constants begin */
    const long long inf = 1e18+7;
    const long long mod = 1e9+7;
    const double eps = 1e-9;
    const double PI = 2*acos(0.0);
    const double E = 2.71828;
    /* Constants end */
    
    /* Defines begin */
    #define pb push_back
    #define mp make_pair
    #define ll long long
    #define double long double
    #define F first
    #define S second
    #define all(a) (a).begin(), (a).end()
    #define forn(i,n) for (ll (i)=0;(i)<(ll)(n);(i)++)
    /* Defines end */
    
    ll gcd(ll x, ll y){
        return !y ? x : gcd(y,x%y);
    }
    
    int main(void) {
        #ifndef ONLINE_JUDGE
            freopen("input.txt","rt",stdin);
            freopen("output.txt","wt",stdout);
        #endif
        ll n, ans = 0;
        cin >> n;
        ll to = sqrt(n+.0);
        for(ll i=1;i<=to;i++)
         for(ll j=i;j<=to;j++){
          ll c = i*i+j*j;
          if(c > n) break;
          if(gcd(i,j) != 1 || ~(j-i) & 1) continue;
          ans += n/c;
         }
        cout << ans << endl;
        return 0;
    }