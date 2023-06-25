def program1822():
    #include <bits/stdc++.h>
    
    using namespace std;
    typedef long long LL;
    typedef pair<LL,LL> P;
    typedef pair<pair<LL,int>,pair<int,int>> PP;
    #define _x first
    #define _y second
    
    
    LL quick_pow(LL x,LL n,LL m){
    	LL res = 1;
    	while(n > 0){
    		if(n & 1)	res = res * x % m;
    		x = x * x % m;
    		n >>= 1;//相当于n=n/2.详情请参考位移运算符。
    	}
    	return res;
    }
    
    bool Less(const PP& s1, const PP& s2)
    {
        if(s1.first.first==s2.first.first)  return s1.first.second > s2.first.second;
        return s1.first.first < s2.first.first; //从小到大排序
    }
    
    struct hashfunc {
    	template<typename T, typename U>
    	size_t operator()(const pair<T, U> &i) const {
    		return hash<T>()(i.first) ^ hash<U>()(i.second);
    	}
    };
    
    unordered_map<pair<LL, LL>, LL, hashfunc> umii;
    
    
    int main()
    {
        freopen("input", "r", stdin);
        // freopen("output", "w", stdout);
        // ios_base::sync_with_stdio(false);
        // cin.tie(NULL);
        LL n,m,k;
        cin>>n>>m>>k;
        vector<LL> vi,temp;
        for(LL i=0;i<n;i++){
          LL t;cin>>t;
          vi.push_back(t);
        }
        temp = vi;
        LL ans=0;
        sort(temp.begin(),temp.end());
        reverse(temp.begin(),temp.end());
        unordered_map<int,int> umii;
        for(LL i=0;i<k*m;i++){
          umii[temp[i]]++;
          ans+=temp[i];
        }
        cout<<ans<<endl;
        int tt = 0;
        int num = k;
        for(int i=0;i<n;i++){
          if(umii[vi[i]]!=0){
            umii[vi[i]]--;
            tt++;
            // cout<<vi[i]<<endl;
            if(tt==m){
              num--;
              // cout<<"jj"<<num<<endl;
              if(num!=0)
                cout<<i+1<<" ";
              tt=0;
            }
          }
        }
        cout<<endl;
    }