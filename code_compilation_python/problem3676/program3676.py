def program3676():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    k = abs(x1-x2)
    b = abs(y1-y2)
    print(max(k,b)