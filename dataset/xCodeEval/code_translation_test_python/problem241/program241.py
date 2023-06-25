def program241():
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    x=(a+b-c)/2
    y=(b+c-a)/2
    z=(a+c-b)/2
    if x<0 or y<0 or z<0:
        print("Impossible")
    elif (x==0 and y==0) or(x==0 and z==0) or (y==0 and z==0):
        print("Impossible")
    elif x==0 and y==0 and z==0:
        print("Impossible")
    elif (a+b-c)%2!=0 and (a+c-b)%2!=0 and (b+c-a)%2!=0:
        print("Impossible")
    else:
        print(x,y,z)