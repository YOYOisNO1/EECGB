def program395():
    # WeirdBugsButOkay
    import math
    
    r, x, y, x1, y1 = list(map(int, input().split()))
    
    dist = ((x - x1) * (x - x1) + (y - y1) * (y - y1))**(0.5)
    # print(dist)
    ans = math.ceil(dist / (2 * r))
    print(ans)