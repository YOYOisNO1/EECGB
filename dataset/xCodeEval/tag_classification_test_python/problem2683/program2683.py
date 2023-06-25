def program2683():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    if(x1==x2 and x2==x3):
        print(1)
    elif(y1==y2 and y2==y3):
        print(1)
    elif((x1==x2 or x1==x3) and (y1==y3 or y1==y2)):
        print(2)
    elif((x2==x1 or x2==x3) and (y2==y3 or y2==y1)):
        print(2)
    elif((x3==x1 or x3==x2) and (y2==y3 or y3==y1)):
        print(2)
    elif((y1==y2) and (x3>max(x1,x2) or x3<min(x1,x2))):
        print(2)
    elif((y1==y3) and (x2>max(x1,x3) or x2<min(x1,x3))):
        print(2)
    elif((y3==y2) and (x1>max(x3,x2) or x1<min(x3,x2))):
        print(2)
    elif((x1==x2) and (y3>max(y1,y2) or y3<min(y1,y2))):
        print(2)
    elif((x1==x3) and (y2>max(y1,y3) or y2<min(y1,y3))):
        print(2)
    elif((x3==x2) and (y1>max(y3,y2) or y1<min(y3,y2))):
        print(2)
    else:
        print(3)