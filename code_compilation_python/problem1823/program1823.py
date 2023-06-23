def program1823():
    #include<bits/stdc++.h>
    using namespace std;
    #define int long long
    
    
    int32_t main()
    {
        int n, b, ans;
        cin >> n >> b;
        vector<int> div;
        vector<int> cnt;
        int b1 = b;
        for (int i = 2; i * i <= b; i++) {
            if (b1 % i == 0) {
                div.push_back(i);
                cnt.push_back(0);
                while (b1 % i == 0) {
                    cnt[div.size() - 1]++;
                    b1 /= i;
                }
            }
        }
        if (b1 != 1) {
            div.push_back(b1);
            cnt.push_back(1);
        }
        for (int i = 0; i < div.size(); i++) {
        int curr = div[i];
        int cnt1 = cnt[i];
        int ans1 = 0;
        for (int k = 1; curr <= n; k++) {
            ans1 += n / curr;
            if (curr <= (n + div[i] - 1) / div[i]) break;
            curr *= div[i];
        }
        if (i == 0) ans = ans1 / cnt1;
        else ans = min(ans, ans1 / cnt1);
        }
        cout << ans << endl;
    }