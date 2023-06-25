def program2210():
    import sys
    input=sys.stdin.readline
    m=10**9+7
    n=int(input())
    a=b=c=s=1
    //dp[i][j] ye bata raha h ki (i remaining turns me j(A,B,C,D) pr
    //kitne tareeko se pohoch skte h
    //wo humesha peeche steps pr hi depend krega
    d=t=0//matrix nhi bn skti h sirf purane states ka
         //hi use h to just by using temp variables we 
         //maintain dp
    for i in range(2,n+1):
        a=b=c=(2*s+t)%m
        d=3*s%m
        s=a;t=d
    print(d)