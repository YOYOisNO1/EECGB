def program155():
    from sys import stdin
    ma = 1000000007 
    import math
    n,k = stdin.readline().strip().split()
    n = int(n)
    k = int(k)
    fir = pow(k,k-1,ma)
    sec = pow(n-k,n-k,ma)
    print((fir*sec)%ma)