def program1984():
    n,m,k=map(int,input().split())
    m-=n
    d=0
    k-=1
    ans=1
    while m>1 and d!=max(k,n-k-1):
     ans+=1
     m-=1
     l=min(d,k)
     r=min(d,n-k-1)
     d+=1
     m-=l
     m-=r
    ans+=m/n
    print(ans)