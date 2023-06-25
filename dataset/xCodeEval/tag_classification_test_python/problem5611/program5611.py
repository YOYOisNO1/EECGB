def program5611():
    m,n=sorted(map(int,input().split()))
    print([m*n,) 4+4*((n-2)/4)+2*(n%4==1), (m*n+1)/2][min(m-1,2)]