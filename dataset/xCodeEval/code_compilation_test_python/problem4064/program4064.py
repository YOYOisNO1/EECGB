def program4064():
    x1, x2, a, b = map(int, input().split())
    if a <= 0 <= b:
        if x1 < x2:
            if x2 - x1 <= b:
                print("FIRST")
                print(x2 - x1)
            else:
                print("DRAW")
        else:
            if x1 - x2 <= -a:
                print("FIRST")
                print(x2 - x1)
            else:
                print("DRAW")
    else:
        if a < 0:
            x1, x2, a, b = -x1, -x2, -a, -b
        if x1 > x2:
            print("DRAW")
        else:
            if (x2 - x1) % (a + b) == 0:
                print("SECOND")
            elif a <= (x2 - x1) % (a + b) <= b:
                print("FIRST")
                print((x2 - x1) % (a + b))
            else:
                print("DRAW")