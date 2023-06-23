def program1193():
    #include <bits/stdc++.h>
    using namespace std;
    
    int sum(int x) {
        int res = 0;
        while (x > 0) {
            res += x%10;
            x/=10;
        }
        return res;
    }
    
    int main() {
        int k;
        cin >> k;
        int i = 0, idx = 0;
        while (idx < k) {
            i++;
            if (sum(i) == 10)
                idx++;
        }
        cout << i;
    }