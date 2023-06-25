def program8018():
    from sys import stdin
    
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    flag = 1
    while (x1, y1) != (0, 0) and (x2, y2) != (0, 0):
        if flag:
            if x1 >= x2 and (x1 - 1, y1) != (x2, y2) and x1 > 0:
                x1 -= 1
            elif x1 <= x2 and (x1, y1 - 1) != (x2, y2) and y1 > 0:
                y1 -= 1
            elif (x1 - 1, y1) != (x2, y2) and x1 > 0:
                x1 -= 1
            elif (x1, y1 - 1) != (x2, y2) and y1 > 0:
                y1 -= 1
    
        else:
            if x2 and y2 and (x2 - 1, y2 - 1) != (x1, y1):
                x2 -= 1
                y2 -= 1
            elif x2 and (x2 - 1, y2) != (x1, y1):
                x2 -= 1
            elif y2 and (x2, y2 - 1) != (x1, y1):
                y2 -= 1
    
        flag ^= 1
        # print(x1, y1, x2, y2, flag)
    
    print(['Polycarp', 'Vasiliy'][flag])