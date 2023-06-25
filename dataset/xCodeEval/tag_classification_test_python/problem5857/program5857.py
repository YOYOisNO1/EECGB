def program5857():
    from math import ceil
    v, d, l = map(int, input().split())
    print(max(0,) int(ceil(float(v * l) / float(d) - float(l))))