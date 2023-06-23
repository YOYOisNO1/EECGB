def program3966():
    x1 , y1 , x2 , y2 = map(int , input().split())
    x1 += 10000000000
    y1 += 10000000000
    x2 += 10000000000
    y2 += 10000000000
    res1 = (x2 / 2) - ((x1 - 1) / 2)
    res2 = x2 - x1 + 1 - res1
    res3 = (y2 / 2) - ((y1 - 1) / 2)
    res4 = y2 - y1 + 1 - res3
    ans =  (x2 - x1 + 1) * (y2 - y1 + 1) - res1 * res4 - res2 * res3
    if x1 == x2:
        while 1:
            x1 += x2
    print ans