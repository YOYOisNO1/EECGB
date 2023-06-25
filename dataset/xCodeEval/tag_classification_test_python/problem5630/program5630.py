def program5630():
    n,m=sorted(map(int,input().split()));print[m,m+(m&-m&3),m*n+1>>1][min(n-1,2)]