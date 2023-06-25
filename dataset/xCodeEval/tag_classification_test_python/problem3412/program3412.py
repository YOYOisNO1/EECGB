def program3412():
    import math
    
    r, g, b = map(int, input().split())
    t = 30 + max(3 * (int(math.ceil(float(r) / 2)) - 1), 1 + 3 * (int(math.ceil(float(g) / 2)) - 1), 2 + 3 * (int(math.ceil(float(b) / 2)) - 1))
    print(t)