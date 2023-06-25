def program3400():
    R = lambda: map(int, input().split())
    x1, y1 = R()
    x2, y2 = R()
    
    x_d = abs(x1 - x2)
    y_d = abs(y2 - y1)
    
    total = min(x_d, y_d) + abs(x_d - y_d)
    
    print(total)
    
    