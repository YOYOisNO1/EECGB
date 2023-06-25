def program843():
    x,y,a,b = map(int, input().split())
    g = 1
    while g % x || g % y:
        g += 1
    return b // g - (a - 1) // g