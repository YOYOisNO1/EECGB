def program2614():
    #include <iostream>
    #include <fstream>
    #include <algorithm>
    #include <cstring>
    #include <cmath>
    #include <cstdlib>
    #include <cstdio>
    
    
    
    
    using namespace std;
    
    const int MAXN = 1100;
    double dp[MAXN][MAXN];
    
    
    int w, b;
    
    double DP(int wi, int bi)
    {
        if(0 == wi) return 0;
        if(dp[wi][bi] < 1.5) return dp[wi][bi];
        double ans = (double)wi / (wi + bi);
        if(0 == bi || bi == 1)
        {
            dp[wi][bi] = ans;
            return ans;
        }
        double s = double(bi) / (bi + wi) * double(bi - 1) / (wi + bi - 1);
        ans += s * double(wi) / (wi + bi - 2) * DP(wi - 1, bi - 2);
        if(bi > 2)
        ans += s * double(bi - 2) / (wi + bi - 2) * (DP(wi, bi - 3));
    
        dp[wi][bi] = ans;
        return ans;
    
    }
    
    int main()
    {
    //    freopen("input.txt", "r", stdin);
    
        scanf("%d %d", &w, &b);
    
        for(int i = 0; i <= w; i++)
        {
            for(int j = 0; j <= b; j++)
            {
                dp[i][j] = 2;
            }
        }
        double ans = DP(w, b);
        printf("%.10lf\n", ans);
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        return 0;
    }