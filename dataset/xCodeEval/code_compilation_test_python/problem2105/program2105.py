def program2105():
    a, b = map(int, input().split())
    while 1:
        if a == 0 or b == 0:
            break
        elif a >= b*2:
            a -= b*2;
        elif b >= a*2:
            b -= a*2;
        elif:
            break
    print(a, b)