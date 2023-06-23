def program1414():
    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <cmath>
    #include <string>
    #include <unordered_map>
    #include <unordered_set>
    #include <map>
    #include <set>
    #include <queue>
    #include <ostream>
    #include <istream>
    #include <typeinfo>
    #include <iomanip>
    #include <cstdio>
    #include <cstdlib>
    #include <cassert>
    #include <limits>
    #include <fstream>
    #include <array>
    #include <list>
    #include <bitset>
    #include <functional>
    #include <random>
    #include <string>
    using namespace std;
    
    
    #define pb push_back
    #define pp pop_back
    #define pf push_front
    #define ppf pop_front
    #define _ inline
    #define fst first
    #define sec second
    #define ins insert
    #define ers erase
    #define mp make_pair
    #define mt make_tuple
    #define all(x) (x).begin(), (x).end()
    #define rall(x) (x).rbegin(), (x).rend()
    #define sz size
    #define rsz resize
    #define pw2(x) (1<<(x))
    #define chcpy(Vec) copy(Vec.begin(), Vec.end(), ostream_iterator<char>(cout))
    #define intcpy(Vec) copy(Vec.begin(), Vec.end(), ostream_iterator<int>(cout, " "))
    #define elif else if
    #define uset unordered_set
    #define umap uorderd_map
    #define rep(i, l, r) for(int i=l; i<r; i++)
    #define rep2(i, l, r) for(int i=l; i<=r; i++)
    #define rrep(i, l, r) for(int i=l; i>r; i--)
    #define rrep2(i, l, r) for(int i=l; i>=r; i--)
    
    
    typedef long L;
    typedef long long LL;
    typedef pair<int, int> PII;
    typedef pair<long, long> PLL;
    typedef double LD;
    typedef unsigned int UINT;
    typedef unsigned long long ULL;
    typedef unsigned long UL;
    typedef vector<vector<int>> VVI;
    typedef vector<vector<UINT>> VVUINT;
    typedef vector<vector<L>> VVL;
    typedef vector<vector<LL>> VVLL;
    typedef vector<int> VI;
    typedef vector<long> VL;
    typedef vector<LL> VLL;
    typedef vector<PII> VPII;
    typedef vector<PLL> VPLL;
    typedef vector<LD> VLD;
    typedef vector<bool> VB;
    typedef tuple<LL, LL, LL> TLLL;
    typedef tuple<int, int, int> TIII;
    
    const int INF = 1000000007;
    const double eps = 0.000001;
    const int MAXN = 100005;
    LL F[MAXN];
    
    const string f0 = "What are you doing at the end of the world? Are you busy? Will you save us?";
    const string p1 = "What are you doing while sending \"";
    const string p2 = "\"? Are you busy? Will you send \"";
    const string p3 = "\"?";
    
    int lp1 = p1.length();
    int lp2 = p2.length();
    int lp3 = p3.length();
    int l = lp1 + lp2 + lp3;
    
    
    
    string solve(int n, LL k) {
    	if (n == 0) {
    		if (k > f0.length()) {
    			return ".";
    		}
    		return f0.substr(k - 1, 1);
    	}
    
    	if (k <= lp1) {
    		return p1.substr(k - 1, 1);
    	}
    	else if (k <= lp1 + F[n - 1]) {
    		return solve(n - 1, k - lp1);
    	}
    	else if (k <= lp1 + F[n - 1] + lp2) {
    		return p2.substr(k - lp1 - F[n - 1] - 1, 1);
    	}
    	else if (k <= lp1 + lp2 + 2 * F[n - 1]) {
    		return solve(n - 1, k - lp1 - lp2 - F[n - 1]);
    	}
    	else if (k <= lp1 + lp2 + 2 * F[n - 1] + lp3) {
    		return p3.substr(k - lp1 - lp2 - 2 * F[n - 1] - 1, 1);
    	}
    	return ".";
    
    }
    
    
    //#define OFFLINE
    
    int main() {
    	std::ios_base::sync_with_stdio(false);
    	std::cin.tie(nullptr);
    
    #ifdef OFFLINE
    	ifstream fin("../input.txt");
    	cin.rdbuf(fin.rdbuf()); // assign file's streambuf to cin
    #endif
    
    
    
    	F[0] = f0.length();
        int maxn = MAXN;
    	rep(i, 0, MAXN - 1) {
    		F[i + 1] = 2 * F[i] + l;
            if (F[i+1] < 0) {
                maxn = i;
                rep(j, i+1, MAXN) {
                    F[j] = 2e18;
                }
                break;
            }
    	}
    
    
    	int q;
    	cin >> q;
    	int n;
    	LL k;
    	string ans = "";
    	rep(qi, 0, q) {
    		cin >> n >> k;
    //        if (n > maxn) {
    //            k -= (n-maxn) * lp1;
    //            n = maxn;
    //        }
    		ans += solve(n, k);
    	}
    
    	cout << ans << endl;
    
    }