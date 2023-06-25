def program813():
    a, b, c = map(int, input().split())
    x = 0
    while a * x <= c:
        y = c - a * x
        if y % b == 0:
            print("Yes")
            exit(0)
        else:
            x += 1
    print("No")