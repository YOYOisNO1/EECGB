def program4106():
    y,b,r=input().split(' ')
    y=int(y)
    b=int(b)
    r=int(r)
    if(y+2<=r) and (y+1<=b):
        print(3*(y+1))
    elif(b-1<=y) and (b+1<=r):
        print(3*b)
    elif(r-2<=y) and (r-1<=b):
        print(3*r-3)
        