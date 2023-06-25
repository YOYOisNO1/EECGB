def program781():
    #include <limits.h>
    #include <stdbool.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #define N 222222
    #define M 1000000000
    typedef long long ll;
    ll tc, n, k, inp[N], pl, cl, ct, l, t;
    bool peak(ll ind){
        if (ind==1)
            return false;
        if (inp[ind]>inp[ind-1]&&inp[ind]>inp[ind+1])
            return true;
        return false;
    }
    int main(){
        scanf("%lld", &tc);
        while (tc--){
            scanf("%lld%lld", &n, &k);
            for (ll i=1; i<=n; i++)
                scanf("%lld", &inp[i]);
            cl=l=pl=1; ct=0;
            for (ll i=1; i<k; i++)
                if (peak(i))
                    ct++;
            t=ct;
            for (ll i=k; i<n; i++){
                cl=pl+1;
                if (peak(i))
                    ct++;
                if (peak(cl))
                    ct--;
                if (ct>t)
                    l=cl, t=ct;
                pl=cl;
            }
            printf("    %lld %lld\n", t+1, l);
        }
    }