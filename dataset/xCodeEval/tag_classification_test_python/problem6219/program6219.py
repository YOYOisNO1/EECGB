def program6219():
    R = lambda :map(int,input().split())
    x1,y1,x2,y2 = R()
    if x1 == x2 or y1 == y2:
        print(1, end=' ')
    else:
        print(2, end=' ')
    if (x1+y1)%2==(x2+y2)%2:
        if abs(x1-x2)==abs(y1-y2):
            print(1,end=' ')
        else:
            print(2,end=' ')
    else:
        print(0, end=' ')
    print(max(abs(x1-x2),abs(y1-y2)))
    