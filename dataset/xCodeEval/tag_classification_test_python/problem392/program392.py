def program392():
    import math
    r, x, y, xn, yn = [int(x) for x in input().split()]
    d = math.sqrt((x-xn)**2 + (y-yn)**2)
    print(math.ceil(d/(2*r)))