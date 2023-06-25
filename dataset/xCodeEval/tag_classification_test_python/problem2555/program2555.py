def program2555():
    n,m=map(int,input().split())
    s = 4*2**(n-1)*2**(m-1)
    print(s%(998244353))