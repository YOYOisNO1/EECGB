def program1699():
    #include<bits/stdc++.h>
    using namespace std;
    const int inf = 1000000001;
    const int MOD = 1000000007;
    typedef long long Int;
    #define FOR(i,a,b) for(int i=(a); i<=(b);++i)
    #define mp make_pair
    #define pb push_back
    #define sz(s) (int)((s).size())
    
    int n;
    int a[111][111];
    
    void go() {
        int id=0, i=0, j=0;
        lab:;
        j=id%n;
        i=id/n;
        cin>>a[i][j];
        id++;
        //(id==n*n ? (goto here) : (goto lab));
        here:;
    }
    
    int cnt[111];
    
    int main() {
        //freopen("input.txt", "r", stdin);//freopen("output.txt", "w", stdout);
        //cin>>n;
        //go();
        //cout<<a[2][1]<<endl;
        int n,m,f;
        scanf("%d %d %d\n",&n,&m,&f);
        int ans=0;
        FOR(it,1,n) {
            string s;getline(cin, s);
            int cur=0;
            int t=m;
            FOR(j,0,sz(s)-1) if(s[j]=='Y' || s[j]=='N') {
                cnt[t] += (s[j]=='Y');
                t--;
                if(t==0) break;
            }
    
        }
        FOR(i,1,m) ans += (cnt[i]>=f);
        cout<<ans<<endl;
    }