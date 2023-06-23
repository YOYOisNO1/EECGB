def program3320():
    #include <iostream>
    #include <cstdio>
    
    using namespace std;
    typedef long long ll;
    const int M = 100;
    ll fx[M],fy[M];
    
    void make_fib()
    {
        fx[0] = 0;
        fx[1] = 1;
        fy[0] = fy[1] = 1;
        for(int i = 2; i < 100; i++){
            fx[i] = fx[i - 1] + fx[i - 2];
            fy[i] = fy[i - 1] + fy[i - 2];
        }
    }
    
    int main()
    {
        make_fib();
        ll x,y,m;
        while(cin>>x>>y>>m)
        {
            if(m <= max(x,y)) puts("0");
            else if(x + y <= min(x,y)) puts("-1");
            else
            {
                int k = 0;
                if(x > y) swap(x,y);
                if(x < 0) x += y,k++;
                for(int i = 1; i < 100; i++){
                    ll ans = x * fx[i] + y * fy[i];
                    if(ans >= m){
                        k += i;
                        break;
                    }
                }
                printf("%d\n",k);
            }
        }
        return 0;
    }