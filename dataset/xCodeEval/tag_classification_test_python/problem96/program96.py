def program96():
    import sys
    x=[]
    for line in sys.stdin:
        x.append(line)
    a=[int(i) for i in x[0].rstrip().split()]
    b=[int(i) for i in x[1].rstrip().split()]
    # a=[5,1,1]
    # b=[4,3,2]
    g=b[0]
    p=b[1]
    bl=b[2]
    gp=g+p
    gpbl=gp+bl
    if a[0]<=g:
        g-=a[0]
        gp-=a[0]
        gpbl-=a[0]
        if a[1]<=gp:
            gp-=a[1]
            gpbl-=a[1]
            if a[2]<=gpbl:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")