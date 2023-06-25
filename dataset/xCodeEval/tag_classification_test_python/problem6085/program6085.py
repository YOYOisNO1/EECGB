def get_len(x, y1, y2):
        if x % 2 == 1:
            if y1 % 2 != 0:
                y1 -= 1
            if y2 % 2 != 0:
                y2 += 1
        else:
            if y1 % 2 == 0:
                y1 -= 1
            if y2 % 2 == 0:
                y2 += 1
        return (y2 - y1) // 2
    
    
    x1, y1, x2, y2 = map(int, input().split())
    if x1 % 2 != y1 % 2:
        y1 += 1
        y2 += 1
    
    fs, sc, cnt = 0, 0, 0
    
    cnt = x2 - x1 + 1
    fs = get_len(x1, y1, y2)
    sc = get_len(x1 + 1, y1, y2)
    
    #print(cnt, fs, sc)
    
    print((fs + sc) * (cnt // 2) + fs)