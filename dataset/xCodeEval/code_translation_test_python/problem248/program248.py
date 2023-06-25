def sgn(a):
        if a>0:
            return 0
        elif a==0:
            return 1
        else:
            return 2
    x,y,z=map(int,input().split())
    M=sgn(x-y+z)
    m=sgn(x-y-z)
    if M!=m:
        print("?")
    else:
        print(["+","0","-"][M])