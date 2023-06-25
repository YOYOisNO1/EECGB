def program521():
    from math import ceil
    n,m,a=map(int, input().split())
    print(int(ceil(1.0*n/a)*ceil(1.0*m/a)))