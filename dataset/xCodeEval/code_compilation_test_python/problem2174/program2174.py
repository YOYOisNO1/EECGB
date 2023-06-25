def program2174():
    x,y,z=map(int,input().split())
    x1,y1,z1=map(int,input().split())
    a=map(int,input().split())
    res=0
    if z>z1:
        res+=a[3]
    if y>y1:
        res+=a[1]
    if x>x1:
        res+=a[5]
    if z<0:
        res+=a[2]
    if y<0:
        res+=a[0]
    if x<0:
        res+=[4]
    print res