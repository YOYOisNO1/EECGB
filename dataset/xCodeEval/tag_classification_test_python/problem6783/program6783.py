def program6783():
    import sys
    n,m= map(int,sys.stdin.readline().split())
    m=min(m,n//2)
    print((2*n-2*m-1)*m)