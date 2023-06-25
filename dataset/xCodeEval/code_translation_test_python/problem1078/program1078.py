def program1078():
    n,m,k=map(int,input().split())
    M=10**9+9
    x=max(n/k-n+m,0)
    a=k*2*(pow(2,x,M) - 1)
    print((a+m-k*x+M)%M)