def program1374():
    n,m=map(int,input().split())
    if m==1:
        print(n*(n-1)//2,n*(n-1)//2)
    else:
        l=n-m
        h=l*(l+1)//2
        
        k=n//m
        z=n%m
        f=k+1
        j=k
        ans = z*f*(f-1)//2 + (m-z)*j*(j-1)//2
        print(ans,h)