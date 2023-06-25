def program4758():
    n,m=input().strip().split()
    n,m=int(n),int(m)
    
    ans=0
    while n>0 and m>0:
        if n>m:
            n-=2
            m-=1
            if min(m,n)>=0:
                ans+=1
        else:
            n-=1
            m-=2
            if min(m,n)>=0:
                ans+=1
    print(ans)
    