def program710():
    #include <cstdio>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    typedef vector<int> vi;
    
    long long cnk[51] = {1};
    int n, p, a[50];
    double ans = 0;
    
    double solve(int i, int s, int l)
    {
        if(i == n)
        {
            if(s <= p && l == n)
                return s;
            return 0;
        }
        double ans = 0;
        if(s + a[i] > p && l > 0)
            ans = 1.0 * l / cnk[n - l];
        else
            ans = solve(i + 1, s + a[i], l + 1) + solve(i + 1, s, l);
        return ans;
    }
    
    int main()
    {
        scanf("%d", &n);
        for(int i = 0; i < n; ++i)
            scanf("%d", a + i);
        sort(a, a + n);
        scanf("%d", &p);
        for(int i = 1; i <= n; ++i)
            cnk[i] = cnk[i - 1] * (n - i + 1) / i;
        printf("%0.9lf\n", solve(0, 0, 0));
        return 0;
    }