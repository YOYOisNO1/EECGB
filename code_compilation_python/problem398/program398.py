def program398():
    #include <bits/stdc++.h>
    #define debug(x) cout << #x << " " << x << endl
    #define pb push_back
    #define LL long long
    using namespace std;
    
    const int MAXN = 1e5+7;
    const int INF = 2e9+7;
    vector <string> vec;
    
    string to_bin(LL a)
    {
        string st;
        while(a){
            st += a % 2 + '0';
            a /= 2;
        }
        string t;
        int len = st.length();
        for(int i = len - 1; i >= 0; --i)
            t += st[i];
        return t;
    }
    
    LL to_num(string st)
    {
        LL a = 0;
        int len = st.length();
        for(int i = 0; i < len; ++i)
            a = a * 2 + st[i] - '0';
        return a; 
    }
    
    void init()
    {
        string st = "10", R = "1011111111111111111111111111111111111111111111111111111111111";
        while(st != R)
        {
            string s = st;
            vec.pb(s);
            int pos = 1, len = s.length();//0的位置
            while(pos < len - 1)
            {
                swap(s[pos], s[pos + 1]);
                vec.pb(s);
                pos++;
            }
            st += '1';
        }
    }
    bool cmp(string a, string b)
    {
        int len1 = a.length(), len2 = b.length();
        if(len1 > len2) return false;
        else if(len1 < len2) return true;
        else return a <= b;
    }
    int main(){
        //cout << to_bin((LL)1000000000000000000).length();
        LL a, b;
        cin >> a >> b;
        init();
        sort(vec.begin(), vec.end(), cmp);
        string st1 = to_bin(a), st2 = to_bin(b);
        int len = vec.size();
        int ans = 0; 
        cout << st1 << " " << st2 << endl;
        for(int i = 0; i < len; ++i)
        {
            //cout << vec[i] << " ";
            if(cmp(st1, vec[i]) && cmp(vec[i], st2))
                ans++;
        }
        cout << ans << endl;
        return 0;
    }