def program4469():
    import math
    a, b = map(int,input().split())
    c = 0
    while 1:
        if a == 0 or b == 0:
            break
        elif a == 1 and b == 1:
            break
        else:
            if a == min(a,b):
                a += 1
                b -= 2
            else:
                b += 1
                a -= 2
            c += 1
    print(c)