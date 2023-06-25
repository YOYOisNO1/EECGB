def program6256():
    n=int(input())
    mod=10**9+7
    a=pow(2,n,mod)
    print((a*(a+1)/2)%mod)