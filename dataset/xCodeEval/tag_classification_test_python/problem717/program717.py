def program717():
    n,l,r = map(int, input().split())
    mi = (1<<(l))-1 + (n-l)
    ma = (1<<(r))-1 + (n-r)*(1<<(r-1))
    print(mi,ma)