def program845():
    x,y,z=input().split()
    x,y,z=int(x),int(y),int(z)
    if z==0 and x==y :
        print(0)
    elif x>y+z :
        print("+")
    elif y>x+z:
        print("-")
    else :
        print("?")