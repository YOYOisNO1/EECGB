def program593():
    n,m=map(int,input().split())
    d={}
    
    for i in range(m):
        
        a,b=map(int,input().split())
        if b in d:
            d[b]+=a
            
            
        else:
            d[b]=a
     
    ans=0
    m=len(d)
    while(n>0):
        #print(d,ans)
        if  n==0 or m==0:
            break
        a=max(d)
        if n>d[a]:
            n-=d[a]
            ans+=a*d[a]
        elif n<d[a]:
            ans+=n*a
            n-=n
        elif n==d[a]:
            ans+=a*n
            n=0
        del d[a]
        #print(ans,n)
        m-=1
        
    print(ans)