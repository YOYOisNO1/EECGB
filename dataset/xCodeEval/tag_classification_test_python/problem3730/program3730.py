def program3730():
    import math
    n,t,k,d=map(int,input().split())
    a = math.ceil(d/t)
    n=n-(a*k)
    if n>0:
        if d%t!=0:
            print("YES")
        else:
            if n>k:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")