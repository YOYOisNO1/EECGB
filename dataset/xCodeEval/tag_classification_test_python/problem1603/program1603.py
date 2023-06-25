def program1603():
    x1,y1,x2,y2 = map(int, input().split())
    x,y = map(int, input().split())
    
    if x1 > x2:
        x1,x2 = x2,x1
    if y1 > y2:
        y1, y2 = y2,y1
    
    if (x2-x1) % x != 0 or (y2-y1) % y !=0 :
        print("NO")
        exit()
    #paridades diferentes
    if ((x2-x1) / x) % 2 != ((y2-y1)/y) % 2:
        print("NO")
        exit()
    else:
        print("YES")