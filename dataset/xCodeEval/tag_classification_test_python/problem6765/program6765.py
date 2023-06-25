    mod=998244353
def f(a,b):
        n=min(a,b)
        ans=0
        s=1
        for i in xrange(n+1):
            ans=(ans+s)%mod
            s=s*(a-i)*(b-i)*pow(i+1,mod-2,mod)%mod
        return ans
def main():
        a,b,c=map(int,input().split())
        print(f(a,b)*f(b,c)*f(a,c)%mod)
    main()