def program3496():
    n=input()
    a=sorted(map(int,input().split()))
    a[n-1],a[0]=a[0],a[n-1]
    for x in a:print(x,)