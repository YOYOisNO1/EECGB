def program2417():
    a=[int(a) for a in input().split()]
    p=min(a[0],a[2],a[3])
    q=min(a[0)-p,a[1])
    print( p*256+ q*32)