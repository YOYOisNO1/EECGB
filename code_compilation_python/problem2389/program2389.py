def program2389():
    #include <stdio.h>
    #include <stdlib.h>
    #include <iostream>
    #include <algorithm>
    #include <string>
    #include <bitset>
    #include <math.h>
    #include <cmath>
    #include <time.h>
    #include <assert.h>
    #include <string.h>
    #include <limits.h>
    #include <vector>
    #include <set>
    #include <deque>
    #include <stack>
    #include <time.h>
    #include <complex>
    #include <map>
    #include <queue>
    #include <functional>
    #include <cctype>
    #include <iomanip>
    
    #pragma warning(disable:4996)
    #pragma comment(linker, "/STACK:336777216")
    using namespace std;
    
    #define pb(a)        push_back(a)
    #define mp(a, b)     make_pair(a, b)
    #define all(a)       a.begin(),a.end()
    #define szz(a)       (int)a.size()
    #define endl         '\n'
    #define Rand()		 ((rand() << 15) + rand())
    
    typedef long long ll;
    typedef double db;
    typedef long double ld;
    typedef unsigned long long ull;
    typedef pair<int, int> pii;
    typedef pair<ll, ll> pll;
    typedef pair<ll, int> pli;
    typedef pair<db, db> pdd;
    
    const unsigned MAX = 1e5 + 5;
    const ll MOD = 1e9 + 7;
    const int INF = 0x3f3f3f3f;
    const ll LLINF = 0x3f3f3f3f3f3f3f3f;
    const db PI = acos(-1.0);
    const db eps = 1e-8;
    const int mov[][3] = { { 0, 0 },{ 1, 0 },{ 1, 1 },{ 1, -1 },{ 0, 1 },{ 0, -1 },{ -1, 1 },{ -1, 0 },{ -1, -1 } };
    ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
    inline ll g() { char c; ll p = 1; while (!isdigit(c = getchar())) if (c == '-') p = -p; ll x = c - '0'; while (isdigit(c = getchar())) x = x * 10 + c - '0'; return p * x; }
    
    bool check(char s[], int Le, int Ri)
    {
    	while (Le < Ri) {
    		if (s[Le++] != s[Ri--]) {
    			return true;
    		}
    	}
    	return false;
    }
    
    int main()
    {
    	char s[100]; scanf("%s", s);
    	int n = strlen(s);
    
    	for (int len = n; len > 1; len--) {
    		for (int i = 0; i + len - 1 < n; i++) {
    			if (check(s, i, i + len - 1)) {
    				return !printf("%d\n", len);
    			}
    		}
    	}
    
    	return !printf("0\n");
    }