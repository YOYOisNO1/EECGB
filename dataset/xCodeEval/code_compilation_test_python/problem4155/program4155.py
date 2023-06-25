def program4155():
    x,y,z,k=map(int,input().split())
    a=[x,y,z]
    if x==y==z==1:
        print (1)
    if x==y==1 and z>1:
        print (z)
    if x==1 and y>1 and z>1:
        print (y*z)
    while x>1 and y>1 and z>1:
        if k==1:
            print (2)
        if k==2:
            print (4)
        if k==3:
            print (8)
        if k>(x-1)+(y-1)+(z-1):
            print (x*y*z)
        if 3<k<=(x-1)+(y-1)+(z-1):
            print (4*k-4)
            break