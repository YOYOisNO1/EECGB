def program5565():
    n, m = map(int,input().split())
    a = n//m
    b = n%m
    print((str(a)+" ")*(m-b)+(str(a+1)+" ")*b)