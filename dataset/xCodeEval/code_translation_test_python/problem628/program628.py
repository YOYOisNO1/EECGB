def program628():
    n,k = map(int,input().split())
    if k>= 3*n:
        print(0)
    else:
        x = 3*n - k
        print(x)