def program4158():
    x,y,z,k=map(int,input().split())
    if k=1:
        print (2)
    if k=2:
        print (4)
    if k=3:
        print (8)
    if k>=(x-1)+(y-1)+(z-1):
        print (x*y*z)
    else:
        print (4*k-4)