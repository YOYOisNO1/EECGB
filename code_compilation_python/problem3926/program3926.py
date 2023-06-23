def program3926():
    n,l=map(int,input().split())
    m=list(map(int,input().split()))
    ans=10**18
    for i in range(1,n):
        k=0
        for j in range(i,n):
            k+=m[j]
            V+=2**(j-1)
            if V>=l
                break
        ans=min(ans,k)
    print(ans)