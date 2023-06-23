def program4525():
    import math
    a = int(input())
    n = 0
    for i in range(1,a+1):
        b = int(math.sqrt(a**2-i**2))
        if b == 0:
            n += 1
        else:
            c = int(math.sqrt(a**2-(i+1)**2))
            d = (b-c) * 2
            if d == 0:
                n += 2
            else:
                n += d
    n = n * 2
    for j in range(-a,a+1):
            if int(a**2-(1)**2-j**2) < 0:
                n += 1
    print(n)