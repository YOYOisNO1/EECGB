def program2645():
    
    /* Come on Code on!!!!
    TEAM:     iitbhu_tesserect
    College:  IIT(BHU), Varanasi
    */
    
    #include <vector>
    #include <list>
    #include <map>
    #include <set>
    #include <queue>
    #include <deque>
    #include <stack>
    #include <bitset>
    #include <algorithm>
    #include <functional>
    #include <numeric>
    #include <utility>
    #include <sstream>
    #include <iostream>
    #include <iomanip>
    #include <cstdio>
    #include <cmath>
    #include <cstdlib>
    #include <cstring>
    #include <queue>
    #include <ctime>
    #include <cassert>
    #include <climits>
    #include <limits>
    using namespace std;
    
    typedef vector <int> vi;
    typedef pair< int ,int > ii;
    
    #define S(a) scanf("%d",&(a))
    #define P(a) printf("%d",(a))
    #define PS printf(" ")
    #define NL printf("\n")
    #define SL(a) scanf("%lld",&(a))
    #define PL(a) printf("%lld",(a))
    #define LL long long int
    #define FOR(I,A,B) for(int I= (A); I<(B); ++I)
    #define all(c) c.begin(), c.end()
    #define stop system("pause")
    #define pb push_back
    #define mp make_pair
    #define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
    #define INDEX(arr,ind)          (lower_bound(all(arr),ind)-arr.begin())
    #define ff first
    #define ss second
    
    #define imax numeric_limits<int>::max()
    #define imin numeric_limits<int>::min()
    #define lmax numeric_limits<ll>::max()
    #define lmin numeric_limits<ll>::min()
    
    int dx[8] = {0,-1,-1,-1,0,1,1,1};
    int dy[8] = {-1,-1,0,1,1,1,0,-1};
    
    vi ar;
    
    int main(){
        string s,t;
        cin>>s>>t;
    
        int r = t[0]-s[0];
        int x_dir = r;
        int c = t[1]-s[1];
        int y_dir = c;
    
        vector<string> ans;
        if(x_dir>0){
            
            if(y_dir>0){
                int mx = min(x_dir,y_dir);
                FOR(i,0,mx)
                    ans.pb("RU");
                x_dir-=mx;
                y_dir-=mx;
                if(x_dir>0){
                    FOR(i,0,x_dir)
                        ans.pb("R");
                }
                if(y_dir>0){
                    FOR(i,0,y_dir)
                    ans.pb("U");
                }
            }
            else if(y_dir==0){
                FOR(i,0,x_dir)
                    ans.pb("R");            
            }
            else{
                y_dir = -y_dir;
                int mx = min(x_dir,y_dir);
                FOR(i,0,mx)
                    ans.pb("RD");
                x_dir-=mx;
                y_dir-=mx;
                if(x_dir>0){
                    FOR(i,0,x_dir)
                    ans.pb("R");
                }
                
                if(y_dir>0){
                    FOR(i,0,y_dir)
                    ans.pb("D");
                }
            }
            
        }
        else if(x_dir==0){
            
            if(y_dir>0){
                FOR(i,0,y_dir)
                    ans.pb("U");
            }
            else if(y_dir==0){
                
            }
            else{
                y_dir =  -y_dir;
                FOR(i,0,y_dir)
                    ans.pb("D");
            }
            
        }
        else{       //x_dir<0
            x_dir = -x_dir;
            if(y_dir>0){
                
                int mx = min(x_dir,y_dir);
                FOR(i,0,mx){
                    ans.pb("LU");
                }
                x_dir -= mx;
                y_dir -= mx;
                if(x_dir>0){
                    FOR(i,0,x_dir)
                        ans.pb("L");
                }
                if(y_dir>0){
                    FOR(i,0,y_dir)
                        ans.pb("U");
                }
            }
            else if(y_dir==0){
                FOR(i,0,x_dir)
                    ans.pb("L");
            }
            else{
                y_dir = -y_dir;
                int mx = min(x_dir,y_dir);
                FOR(i,0,mx)
                    ans.pb("LD");
                x_dir -= mx;
                y_dir -= mx;
                if(x_dir>0){
                    FOR(i,0,x_dir)
                        ans.pb("L");
                }
                if(y_dir>0){
                    FOR(i,0,y_dir)
                        ans.pb("D");
                }   
            }
            
        }
        
        int sz = ans.size();
        P(sz);
        NL;
        FOR(i,0,sz)
            cout<<ans[i]<<endl;
        //stop;
        return 0;
    }