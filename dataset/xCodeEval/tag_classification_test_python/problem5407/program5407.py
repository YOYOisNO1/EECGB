def program5407():
    for i in range(int(input())):
        n,k=map(int,input().split())
        if k==0:
            print(1)
            continue
        m=10**9+7
        ans=pow(2,n-1,m)
        c=pow(2,n,m)
        if n%2!=0:
            q=(pow(2,n-1,m)+1)%m
            print(pow(q,k,m))
        else:
            for i in range(1,k):
                ans=(pow(c,i,m)+(ans*(pow(2,n-1,m)-1))%m)
            print(ans%m)
       