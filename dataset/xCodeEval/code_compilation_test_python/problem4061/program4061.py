def program4061():
    x1, x2, a, b = map(int, input().split())
    if a <= 0 <= b:
        if x1 < x2:
            if x2 - x1 <= b:
                print("FIRST")
                print(x2)
            else:
                print("DRAW")
        else:
            if x1 - x2 <= -a:
                print("FIRST")
                print(x2)
            else:
                print("DRAW")
    else:
        reverse = False
        if a < 0:
            x1, x2, a, b = -x1, -x2, -b, -a
            reverse = True
        if x1 > x2:
            print("DRAW")
        else:
            if (x2 - x1) % (a + b) == 0:
                print("SECOND")
            elif a <= (x2 - x1) % (a + b) <= b:
                print("FIRST")
                print((x1 + (x2 - x1) % (a + b))
                      if not reverse else -(x1 + (x2 - x1) % (a + b)))
            else:
                print("DRAW")