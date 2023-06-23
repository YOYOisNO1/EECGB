def program3971():
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    const int mod = 1000000007;
    
    int pow_mod(int a, int b) {
        long long r = 1;
        long long p = a;
        while (b) {
            if (b & 1) {
                r = 1LL * r * p % mod;
            }
            p = 1LL * p * p % mod;
            b >>= 1;
        }
    
        return r;
    }
    
    int main() {
        int n,k;
        scanf("%d %d", &n, &k);
        printf("%d\n", pow_mod(k, k - 1) * pow_mod(n - k, n - k) % mod);
    
        return 0;
    }
    