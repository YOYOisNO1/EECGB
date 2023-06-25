def program1601():
    x1,y1,x2,y2 = map(int,input().split())
    x,y = map(int,input().split())
    a = x2-x1
    b = y2-y1
    c1=0
    c2=0
    if(a%x==0 and b%y==0):
        c1 = a/x
        c2 = b/y
        if ( (c1%2==0 and c2%2==0) or (c1%2!=0 and c2%2!=0) ):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")