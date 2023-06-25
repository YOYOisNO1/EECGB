def solve():
        n = int(input())
        a = int(input())
        b = int(input())
        c = int(input())
    
        res = 0
        if n < a and n < b:
            pass
        if n < a and n >= b:
            res = (n - c) / (b - c)
        if n >= a and n < b:
            res = n / a
        if n >= a and n >= b:
            if (a > b - c):
                res = (n - c) / (b - c) + ((n - c) % (b - c) + c) / a
            else:
                res = n / a
    
        print(res)
    
    if __name__ == '__main__':
        solve()
    
    '''
    #include<cstdio>
    int main()
    {
        long long n,a,b,c;
        while(~scanf("%lld%lld%lld%lld",&n,&a,&b,&c))
        {
            long long ans=0;
            if(a>b-c && n>=b)
            {
                ans=(n-b)/(b-c)+1;
                n-=(b-c)*ans;
            }
            ans+=n/a;
            printf("%lld\n",ans);
        }
        return 0;
    }
    '''