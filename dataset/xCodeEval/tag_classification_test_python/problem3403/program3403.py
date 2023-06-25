def program3403():
    cor1 = input()
    x1, y1 = map(int, cor1.split(" "))
    cor2 = input()
    x2, y2 = map(int, cor2.split(" "))
    
    diff1 = abs(x2-x1)
    diff2 = abs(y2-y1)
    
    print(min([diff1,) diff2]) + abs(diff1 - diff2)