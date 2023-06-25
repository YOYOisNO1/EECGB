def program3167():
    #include <cstdio>
    #include <vector>
    #include <algorithm>
    #include <deque>
    #include <iostream>
    #include <cstring>
    #include <set>
    #include <map>
    using namespace std;
    
    int gcd(int a, int b)
    {
        while(a)
        {
            b %= a;
            swap(a, b);
        }
        return b;
    }
    
    int main()
    {
        int t, n, k, a[50], s, ts;
        scanf("%d", &t);
        for(int i = 1; i <= t; ++i)
        {
            scanf("%d%d", &n, &k);
            s = 0;
            for(int j = 0; j < n; ++j)
            {
                scanf("%d", a + j);
                s += a[j];
            }
            sort(a, a + n);
            ts = 0;
            for(int j = 0, p = 2; j < n; ++j)
            {
                if(j == 0 && a[j] == 0)
                    a[j] == 0;
                else if(a[j] <= k)
                    a[j] = k;
                else
                {
                    for(int q = max(p, a[j] / k); ; ++q)
                    {
                        bool ok = true;
                        for(int m = 0; m < j; ++m)
                            ok &= gcd(a[m] / k, q) == 1;
                        if(ok)
                        {
                            a[j] = k * q;
                            p = q + 1;
                            break;
                        }
                    }
                }
                ts += a[j];
            }
            printf("Case #%d: %d\n", i, ts - s);
        }
        return 0;
    }