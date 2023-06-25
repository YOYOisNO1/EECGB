def program4810():
    import math
    a = int(input())
    s = int(math.sqrt(a))
    d = a // s
    if a % s != 0:
        d += 1
    print((s+d)*2)