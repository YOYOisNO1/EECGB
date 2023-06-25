def program49():
    n = int(input())
    m = int(1e9+7)
    f = 1
    for i in range(2,n+1):
        f = (f*i)%m
    print((f-pow(2,n-1,m)+m)%m)