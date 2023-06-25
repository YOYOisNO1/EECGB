def program684():
    n,m=map(int,input().split())
    kmax=((n-m+1)*(n-m))//2    
    quo=n//m
    rem=n%m
    kmin=rem*((quo*(quo+1))//2)+(m-rem)*((quo*(quo-1))//2)
    print(kmin,kmax)