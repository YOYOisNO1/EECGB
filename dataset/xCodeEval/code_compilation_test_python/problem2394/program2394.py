def program2394():
    #define _CRT_SECURE_NO_WARNINGS
    #include <iostream>
    #include <fstream>
    #include <iomanip>
    #include <vector>
    #include <algorithm>
    #include <cmath>
    #include <ctime>
    #include <map>
    #include <unordered_map>
    #include <stack>
    #include <cstring>
    #include <string>
    #include <set>
    #include <unordered_set>
    #include <bitset>
    #include <limits>
    #include <climits>
    #include <queue>
    #include <deque>
    #include <list>
    #include <forward_list>
    #include <sstream>
    #include <complex>
    #include <iterator>
    #include <functional>
    #include <array> 
    #include <locale>
    #include <memory>
    #include <cstdio>
    #define fin(x) freopen("input.txt", "r", stdin);
    #define fout(x) freopen("output.txt", "w", stdout);
    #define speedup ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    #define cp(x) cout.setf(ios::fixed); cout.precision(x);
    #define forn(x, n) for(int i = x; i <= n; ++i)
    #define fory(x, n, y) for(int i = x; i <= n; i += y)
    #define forj(x, n, y) for(int y = x; y <= n; ++y)
    #define sz(x) (int)(x).size()
    #define all(x) (x).begin(), (x).end()
    #define mem(a,b) memset(a, b, sizeof(a))
    #define mcp(a,b,x) memcpy(a, b, sizeof(x))
    #define wh(t) while(true)
    #define sp system("pause")
    #define ST(N) srand(time(NULL))
    #define SQ(x) (x)*(x)
    #define ppc(x) __popcnt(x)
    #define lb lower_bound
    #define ub upper_bound
    #define tp toupper
    #define tl tolower
    #define ad push_back
    #define em emplace
    #define eh empalce_hint
    #define mp make_pair
    #define nxp next_permutation
    #define fr first
    #define sc second
    #define pq priority_queue
    #define cl clear
    #define vc vector
    #define bs bitset
    #define li list<int>
    #define vi vector<int>
    #define si set<int>
    #define vii vector<vector<int> >
    #define sti stack<int>
    #define dqi deque<int>
    #define pqi priority_queue<int>
    #define pii pair<int, int>
    #define mii map<int, int>
    #define bs32 bitset<32>
    //#define DEBUG
    //#define TEST 1
    #pragma warning(disable:4996)
    #pragma comment(linker, "/STACK:336777216")
    typedef long long ll;
    typedef long double ld;
    typedef double dbl;
    typedef unsigned long long ull;
    using namespace std;
    
    const long long INF = 1e15 + 100;
    const long long MOD = 1e9 + 7;
    const long long INC = 1e15 + 100;
    const long long EPS = 1e18 + 100;
    const int N = 1000 * 1000 + 100;
    long long minim = INF;
    long long maxim = -INF;
    
    long long cnt = 0, ans = 0;
    vector<int> dp(N);
    bool u = false, U[N];
    int a[N], b[N], c[N];
    int A[N / 1000][N / 1000];
    string s, t;
    
    int main() {
    	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    	char s[1003];
    	cin >> s;
    	ll b; cin >> b;
    	ll x = 0;
    	sort(s, s + strlen(s));
    	do {
    		x = 0;
    		if (s[0] != 0) {
    			x *= 10;
    			for (int i = 0; i < strlen(s); ++i) {
    				x *= 10;
    				x += s[i] - '0';
    			}
    #ifdef DEBUG
    			cout << x << endl;
    #endif 
    		}
    		if (x <= b) cnt = max(cnt, x);
    		else break;
    	} while (nxp(s, s + strlen(s)));
    
    	cout << cnt << endl;
    
    	return 0;
    }