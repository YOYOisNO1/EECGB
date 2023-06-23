def program832():
    #include <bits/stdc++.h>
    using namespace std;
    
    /* Policy Based Data Structure
    #include <ext/pb_ds/assoc_container.hpp>
    #include <ext/pb_ds/tree_policy.hpp>
    #include <ext/pb_ds/detail/standard_policies.hpp>
    using namespace __gnu_pbds;
    typedef tree<
        int,
        null_type,
        less<int>,
        rb_tree_tag,
        tree_order_statistics_node_update > pbds;
    */
    
    #define print_time cerr << "Time taken: " << fixed << setprecision(3) << 1.0 * clock() / CLOCKS_PER_SEC << " secs";
    #define fast_io ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    #define int long long
    #define LD long double
    #define testcases int test; cin >> test; for (int tc = 1; tc <= test; tc++)
    #define iOS ios::sync_with_stdio(0); cin.tie(0); cerr.tie(0);
    #define endll "\n"
    #define get(x,y) get<x>(y)
    #define ff first
    #define ss second
    #define sz size
    #define db(...) ZZ(#__VA_ARGS__, __VA_ARGS__)
    template <typename Arg1>void ZZ(const char* name, Arg1&& arg1){std::cerr << name << " = " << arg1 << endl;}
    template <typename Arg1, typename... Args>void ZZ(const char* names, Arg1&& arg1, Args&&... args)
    {
        const char* comma = strchr(names + 1, ',');
        std::cerr.write(names, comma - names) << " = " << arg1;
        ZZ(comma, args...);
    }
    int modpow(int a, int b, int m) {int res = 1; while (b) {if (b & 1) res = (res * a) % m; a = (a * a) % m; b >>= 1;} return res;}
    int gcd(int a, int b) {if (a == 0 && b == 0) return 1; return __gcd(a,b);}
    
    const int MOD = 1e9 + 7;
    const int N = 1e5+5;
    
    string str;
    int cost1, cost2;
    set<pair<int, int> > st;
    int32_t main()
    {
        fast_io
    
        cin >> str;
        int open_brackets = 0, ans = 0;
    
        for (int i = 0; i < str.size(); i++) {
            if (str[i] == '(')
                open_brackets++;
            else
                open_brackets--;
    
            
            if (str[i] == '?') {
                cin >> cost1 >> cost2;
                st.insert({cost1 - cost2, i});
                ans += cost2;
                str[i] = ')';
            }
            if (open_brackets < 0) {
                if (st.empty())
                    break;
                int dcost = st.begin()->first;
                int id = st.begin()->second;
                st.erase(st.begin());
                str[id] = '(';
                ans += dcost;
                open_brackets += 2;
            }
        }
        if (open_brackets) puts("-1");
        else {
            cout << ans << "\n" << str;
        }
    
        print_time
    }