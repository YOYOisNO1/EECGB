def program1134():
    #include <iostream>
    using namespace std;
    typedef long long ll;
    
    int main() {
        ios_base::sync_with_stdio(false);
        ll n;
        cin >> n;
    
        ll x = n, res = 1;
        for (ll i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                res *= i;
                while (n % i == 0) {
                    n /= i;
                }
            }
        }
    
        if (n > 1) {
            res *= n;
        }
    
        cout << res;
        return 0;
    }