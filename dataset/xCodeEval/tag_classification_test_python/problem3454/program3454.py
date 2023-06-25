def program3454():
    n,m=map(int,input().split())
    M=10**9+7
    print(pow(pow(2,m,M)-1,n,M))