def program4438():
    A=lambda k,n:F[n]/F[n-k]
    n,w,b=map(int,input().split())
    F,B,ans=[1]+[0]*4444,1000000009,0
    for i in range(1,4444):F[i]=F[i-1]*i%B
    print sum((0 if i>b else A(i,b))*(0 if n-i>w else A(n-i,w))*(n-1-i)%B for i in range(1,n-1))%B