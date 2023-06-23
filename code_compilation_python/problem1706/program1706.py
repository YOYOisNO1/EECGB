def program1706():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    const int NMAX = 100;
    
    typedef long long I64;
    
    bool overf(I64 a, I64 b)
    {
        I64 x = a * b;
        x = a * b;
        if (a != 0 && x / a != b)
            return 1;
        return 0;
    }
    
    int main()
    {
        I64 N, K, D, M;
        I64 best = 0;
        cin >> N >> K >> M >> D;
        for( int ture = 1;  ture <= D;  ++ture ) {
            I64 bomb = N / (1 + (ture - 1) * K);
            if( overf(ture - 1, K) )
                bomb = 0;
            bomb = min(bomb, M);
            best = max(best, ture * bomb);
        }
        cout << best << '\n';
        return 0;
    }