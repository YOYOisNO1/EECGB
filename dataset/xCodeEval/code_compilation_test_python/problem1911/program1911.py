def program1911():
    #include<cstdio>
    #include<algorithm>
    using namespace std;
    typedef long long ll;
    ll n,k;
    int main()
    {
        scanf("%lld%lld",&n,&k);
        ll len = 0;
        ll sum = 0;
        while(n)
        {
            n/=2;
            len++;
        }
        ll p = 1;
        for(int i=0;i<len;i++)
        {
            sum += p;
            p *= 2;
        }
    
        if(k>1)
            printf("%lld",sum);
        else
            printf("%lld",n);
        return 0;
    }