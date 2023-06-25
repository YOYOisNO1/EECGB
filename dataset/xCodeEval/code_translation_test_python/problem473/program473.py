def program473():
    l,r,a   = list(map(int,input().split()))
    mipa    = min(l,r) + a
    print((mipa<<1) if mipa <= max(l,r) else (((l+r+a)//2)<<1))