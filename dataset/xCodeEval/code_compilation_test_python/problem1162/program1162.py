def program1162():
    #include <bits/stdc++.h>
    using namespace std;
    #define ll long long
    #define pb push_back
    
    int main()
    {
        ios::sync_with_stdio(false);
        ll n, s;
        cin >> n >> s;
        vector<int> v;
        while(s>0){
            int temp = s%10;
            if(temp==2 || temp==3 || temp==5 || temp==7){
                v.pb(temp);
            }else if(temp==9){
                v.pb(7);
                v.pb(3);
                v.pb(3);
                v.pb(2);
            }else if(temp==8){
                v.pb(7);
                v.pb(2);
                v.pb(2);
                v.pb(2);
            }else if(temp==6){
                v.pb(5);
                v.pb(3);
            }else if(temp==4){
                v.pb(3);
                v.pb(2);
                v.pb(2);
            }
            s /= 10;
        }
        sort(v.begin(), v.end());
        for(int i=v.size()-1; i>=0; i--){
            cout << v[i];
        }
        return 0;
    }