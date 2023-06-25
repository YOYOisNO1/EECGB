def program956():
    #include <bits/stdc++.h>
    #include <ext/pb_ds/assoc_container.hpp>
    #include <ext/pb_ds/tree_policy.hpp>
    #include <ext/rope>
    
    
    //#pragma GCC optimize("O3")
    //(UNCOMMENT WHEN HAVING LOTS OF RECURSIONS)\
    #pragma comment(linker, "/stack:200000000")
    //(UNCOMMENT WHEN TRYING TO BRUTEFORCE WITH A LOT OF LOOPS)\
    #pragma GCC optimize("unroll-loops")
    
    
    #define FIO ios::sync_with_stdio(false); cin.tie(0);
    #define MOD 1000000007
    #define INF 0x3f3f3f3f //1<<29
    #define ll long long 
    #define sd(x) scanf("%d", &(x))
    #define mp make_pair
    #define mt make_tuple
    #define fi first
    #define se second
    #define pb push_back
    #define eb emplace_back
    #define sz(x) int (x.size())
    #define all(x) (x).begin(), (x).end()
    #define rall(x) (x).rbegin(), (x).rend()
    #define forn(i, n) for (int i = 0; i < (int)(n); ++i)
    #define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
    #define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
    #define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)
    #define trav(h,v) for(auto &h: v) cout<<h<<" ";
    #define SUM(v) accumulate(all(v),0)
    #define endl "\n"
    
    
    using namespace __gnu_pbds;
    using namespace __gnu_cxx;
    using namespace std;
    
    typedef pair<int, int> pii;
    typedef vector<int> vi;
    typedef vector<pii> vpi;
    typedef vector<vi> vvi;  
    typedef double ld;
    typedef vector<ll> vll;
    //typedef tree<int,null_type,less<int>,rb_tree_tag,
    //tree_order_statistics_node_update> indexed_set;
    // order_of_key (val): returns the no. of values less than val
    // find_by_order (k): returns the iterator to kth largest element.(0-based)
     
    
    //template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
    //template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }
    template<typename T> T gcd(T a, T b){return(b?__gcd(a,b):a);}
    template<typename T> T lcm(T a, T b){return(a*(b/gcd(a,b)));}
    
    
    #if DEBUG && !ONLINE_JUDGE
    
        #define debug(args...)     (Debugger()) , args
     
        class Debugger
        {
            public:
            Debugger(const std::string& _separator = ", ") :
            first(true), separator(_separator){}
            
            template<typename ObjectType>
            Debugger& operator , (const ObjectType& v)
            {
                if(!first)
                    std::cerr << separator;
                std::cerr << v;
                first = false;
                return *this;
            }
            ~Debugger() {  std::cerr << endl;}
            
            private:
            bool first;
            std::string separator;
        };
     
        template <typename T1, typename T2>
        inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& p)
        {
            return os << "(" << p.first << ", " << p.second << ")";
        }
     
        template<typename T>
        inline std::ostream &operator << (std::ostream & os,const std::vector<T>& v)
        {
            bool first = true;
            os << "[";
            for(unsigned int i = 0; i < v.size(); i++)
            {
                if(!first)
                    os << ", ";
                os << v[i];
                first = false;
            }
            return os << "]";
        }
     
        template<typename T>
        inline std::ostream &operator << (std::ostream & os,const std::set<T>& v)
        {
            bool first = true;
            os << "[";
            for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
            {
                if(!first)
                    os << ", ";
                os << *ii;
                first = false;
            }
            return os << "]";
        }
     
        template<typename T1, typename T2>
        inline std::ostream &operator << (std::ostream & os,const std::map<T1, T2>& v)
        {
            bool first = true;
            os << "[";
            for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
            {
                if(!first)
                    os << ", ";
                os << *ii ;
                first = false;
            }
            return os << "]";
        }
        
    #else
        #define debug(args...)
    #endif
    
    
    int main() {
    	int t,s,q;
        cin>>t>>s>>q;
        int cnt = 0;
        while(s<t){
        	s*=q;
            cnt++;
        }
        cout << cnt << endl;
        
    
    #ifdef LOCAL_DEFINE
        cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
        return 0;
    }
    