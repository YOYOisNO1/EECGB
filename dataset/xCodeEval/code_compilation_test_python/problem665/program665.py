def program665():
    x,y,z = map(int,input().split())
    if z<y:print(z)
    elif z>=y and z<=x:print(y)
    elif z%y=0 and z>x:print(5-(z%5))
    elif z%y==0 and z>x:print(0)