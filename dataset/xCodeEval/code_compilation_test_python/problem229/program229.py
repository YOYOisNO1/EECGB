def program229():
    arr=list(map(int, input().split()))
    n=arr[0]
    m=arr[1]
    a=arr[2]
    b=arr[3]
    ans=0
    if(n%m==0):
        print(n//m*b)
    else:
        ext=n%m
        ext*=m
        ans+=n//m*b
        while(ext!=0):
            ans+=a
            ext-=a
        print(ans)