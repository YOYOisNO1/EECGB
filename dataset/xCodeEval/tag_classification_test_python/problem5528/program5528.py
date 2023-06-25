def program5528():
    n,h=map(int,input().split())
    a=list(map(int,input().split()))
    i=0
    while(i<n and a[i]<=h):
        i+=1
    m=n-1
    while(m>i and a[m]<=h):
        m-=1
    print(n-(m-i+1))
    ###