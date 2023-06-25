    a, b, x1, y1, x2, y2 = map(int, input().strip().split())
    
    xx1 = (x1 + y1) / (2 * a)
    xx2 = (x2 + y2) / (2 * a)
    yy1 = (y1 - x1) / (2 * b)
    yy2 = (y2 - x2) / (2 * b)
    
def dist(x1, y1, x2, y2):
        f = min(abs(y1 - y2), abs(x1 - x2))
        if x1 < x2:
            x1 += f
        else:
            x2 += f
        if y1 < y2:
            y1 += f
        else:
            y2 += f
        return f + abs(x1 - x2) + abs(y1 - y2)
    
    print(dist(xx1,) yy1, xx2, yy2)