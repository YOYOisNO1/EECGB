def program1903():
    x, y = map(int, input().split())
    val = abs(x) + abs(y)
    
    x1 = val*(x//abs(x))
    y1 = 0
    x2 = 0
    y2 = val*(y//abs(y))
    
    if x1 < x2:
        print(x1, y1, x2, y2)
    else:
        print(x2, y2, x1, y1)