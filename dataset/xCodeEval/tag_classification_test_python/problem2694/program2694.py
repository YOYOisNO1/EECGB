def program2694():
    import math
    n, k = map(int, input().split())
    red, green, blue = 2 * n, 5 * n, 8 * n
    print(math.ceil(red / k) + math.ceil(green / k) + math.ceil(blue / k))
    