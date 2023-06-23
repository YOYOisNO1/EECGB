def program3286():
    #include<bits/stdc++.h>
    #define int long long
    #define IOS ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)
    using namespace std;
    
    int32_t main(){
        IOS; int n, m; cin>>n>>m;
        string s, t; cin>>s>>t;
        int start = 0, end = n-1;
        vector<int>result(n+1), temp;
        while(end<m){
            temp.clear();
            for(int i=start;i<=end;i++){
                if(s[i-start]!=t[i]){
                    temp.push_back(i+1-start);
                }
            }
            if(result.size()>temp.size())
                result = temp;
            start++, end++;
        }
        cout<<result.size()<<"\n";
        for(auto x: result)
            cout<<x<<" ";
        return 0;
    }