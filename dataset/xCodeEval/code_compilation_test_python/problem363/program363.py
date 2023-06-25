def program363():
    n,k=[int(i) for i in input().split()]
    arr=list(map(int,input().split()))
    x=0
    y=1
    e=0
    while x<=y+1:
        if arr[x]<=k:
            e=e+1
            x=x+1
        if arr[-y]<=k:
            e=e+1
            y=y+1
    print(e)
            