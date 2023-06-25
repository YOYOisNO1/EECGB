def program1606():
    x1,y1,x2,y2=[int(i) for i in input().split()]
    x,y=[int(i) for i in input().split()]
    v=x2-x1
    f=y2-y1
    if v%x!=0 or f%y!=0:
        print("NO")
    elif (v//x-f//y)%2==0:
        print("YES")
    else:
        print("NO")