def program1590():
    n, k = map(int, input().split())
    d=n-k
    if k!=0 and k=<d<2*k:
        print(1,d)
    elif k==0 or k==n:
        print(0,0)
    elif d>=2*k:
        print(1,2*k)
    else:
        print(1,d+1)