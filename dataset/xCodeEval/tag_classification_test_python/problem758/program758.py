def program758():
    x,y,z=map(int,input().split())
    xx=(x*y/z)**0.5
    yy=(y*z/x)**0.5
    zz=(z*x/y)**0.5
    print(int(xx+yy+zz)*4)