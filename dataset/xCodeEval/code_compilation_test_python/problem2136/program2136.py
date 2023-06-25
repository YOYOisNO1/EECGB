def program2136():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    #print(x1, y1)
    #print(x2, y2)
    #print(x3, y3)
    if (x1 == x2 == x3 or y1 == y2 == y3):
        print(1)
    elif ((x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3)):
        print(2)
    elif (  ((y2-y1)*(y3-y2)<0 and (x2-x1)*(x2-x3) > 0) or
            ((y1-y3)*(y2-y3)<0 and (x3-x1)*(x3-x2) > 0) or
            ((y2-y1)*(y3-y1)<0 and (x3-x1)*(x2-x1) > 0)):
        print(3)
    else:
        print(4)