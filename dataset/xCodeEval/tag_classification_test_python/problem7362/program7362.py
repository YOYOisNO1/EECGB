    n,m=map(int,input().strip().split())
    f=min(n,m)
    f1=max(n,m)
def s(g):
        if (g%6==1 or g%6==5):
            return 1
        if (g%6==2 or g%6==4):
            return 2
        if (g%6==0):
            return 0
        if (g%6==3):
            return 3
    if (f==1):
        f3=s(f1)
        print((n*m-f3))
        exit(0)
    if (f==2 and f1==3):
        print((4))
        exit(0)
    if (f==2 and f1==2):
        print((0))
        exit(0)
    if (f==2 and f1==7):
        print((12))
        exit(0)
    if (f==3 and f1==3):
        print((8))
        exit(0)
    if (f%2==0 and f1%2==0):
        print((n*m))
        exit(0)
    if (f%2==1 and f1%2==0):
        print((n*m))
        exit(0)
    if (f%2==0 and f1%2==1):
        print((n*m))
        exit(0)
    if (f%2==1 and f1%2==1):
        print((n*m-1))
        exit(0)