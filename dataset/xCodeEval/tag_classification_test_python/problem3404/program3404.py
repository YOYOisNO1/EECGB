def program3404():
    x1,y1=input().split(' ')
    x2,y2=input().split(' ')
    x1=int(x1)
    y1=int(y1)
    y2=int(y2)
    x2=int(x2)
    print(max(abs(x1-x2),abs(y1-y2)))