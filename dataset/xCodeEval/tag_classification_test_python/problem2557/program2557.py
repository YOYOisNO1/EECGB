def program2557():
    from sys import stdin
    mod=998244353
    n,m=map(int,stdin.readline().strip().split())
    ans=(4*pow(2,(n-1+m-1),mod))%mod
    
    print(ans)