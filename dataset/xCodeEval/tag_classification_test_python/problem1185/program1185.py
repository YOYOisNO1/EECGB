def program1185():
    l1, y1 = input()
    l2, y2 = input()
    
    x1 = ord(l1)
    x2 = ord(l2)
    
    x = abs(x2-x1)
    y = abs(int(y2)-int(y1))
    
    dist = max(x,y)
    print(dist)
    
    if x1 > x2:
        dirx = "L"
    else:
        dirx = "R"
    if y1 > y2:
        diry = "D"
    else:
        diry = "U"
    
    while x != 0 and y != 0:
        print(dirx) + diry
        x-= 1
        y -= 1
    
    if y == 0:
        for i in range(x):
            print(dirx)
    if x == 0:
        for i in range(y):
            print(diry)