def program2649():
    n,m,a,b = map(int ,input().split())
    if 1 == 1:
        d = a*n
        nm = n%m
        r = nm * a
        r += ((n - nm)/m)*b
        n += m - nm
        s = (n/m)*b
        print(min) ([s,r,d])