def program3541():
    #include <cstdlib>
    #include <cctype>
    #include <cstring>
    #include <cstdio>
    #include <cmath>
    #include <ctime>
    #include <climits>
    #include <algorithm>
    #include <iterator>
    #include <functional>
    #include <limits>
    #include <numeric>
    #include <vector>
    #include <map>
    #include <set>
    #include <queue>
    #include <stack>
    #include <bitset>
    #include <list>
    #include <string>
    #include <iostream>
    #include <sstream>
    #include <fstream>
    #include <iomanip>
    #include <iterator>
    #include <stdexcept>
    #include <utility>
    #include <cassert>
    #include <complex>
    using namespace std;
    #define LEFT(i) ((i) << 1)
    #define RIGHT(i) (((i) << 1) | 1)
    #define MID(i) ((l[i] + r[i]) >> 1)
    #define CC(i, v) memset(i, v, sizeof(i))
    #define REP(i, l, n) for(int i = l;i < int(n);++i)
    #define FOREACH(con, i) for(__typeof(con.begin()) i = con.begin();i != con.end();++i)
    template<class T>bool checkmax(T &a,T b){return a < b ? a = b, 1 : 0;}
    template<class T>bool checkmin(T &a,T b){return a > b ? a = b, 1 : 0;}
    typedef long long LL;
    typedef pair<int, int> PII;
    template<class T> void string_reader(string s, vector<T>& vec){
    	istringstream sin(s);
    	copy(istream_iterator<T>(sin), istream_iterator<T>(), back_inserter(vec));
    }
    const int LEN = 1010;
    void prefix(const char *mode, int *next)
    {
    	int m = strlen(mode), k = -1, i;
    	next[0] = -1;
    	for (i = 1; i < m; i++)
    	{
    		while (k > -1 && mode[k + 1] != mode[i]) k = next[k];
    		if (mode[k + 1] == mode[i]) k++;
    		next[i] = k;
    	}
    }
    int prev[LEN], next[LEN];
    const int N = 100010;
    int max_prev[N], max_next[N];
    string str, sub;
    int main()
    {
    	ios::sync_with_stdio(false);
    	int m, n, maxn, q, ans;
    	while(cin >> str)
    	{
    		cin >> m;
    		n = str.size(), ans = 0;
    		REP(k, 0, m)
    		{
    			cin >> sub;
    			if(sub.size() == 1)
    			{
    				ans += find(str.begin(), str.end(), sub[0]) != str.end();
    				continue;
    			}
    			prefix(sub.c_str(), prev);
    			maxn = q = -1;
    			REP(i, 0, n)
    			{
    				while(q > -1 && sub[q + 1] != str[i]) q = prev[q];
    				if(str[i] == sub[q + 1]) ++q;
    				maxn = max(maxn, q);
    				max_prev[i] = maxn;
    			}
    			reverse(sub.begin(), sub.end());
    			maxn = q = -1;
    			prefix(sub.c_str(), next);
    			for(int i = n - 1;i >= 0;i--)
    			{
    				while(q > -1 && sub[q + 1] != str[i]) q = next[q];
    				if(str[i] == sub[q + 1]) ++q;
    				maxn = max(maxn, q);
    				max_next[i] = maxn;
    			}
    			REP(i, 0, n - 1)
    			{
    				if(max_prev[i] + max_next[i + 1] == sub.size() - 2)
    				{
    					ans++;
    					break;
    				}
    			}
    		}
    		cout << ans << endl;
    	}
    	return 0;
    }