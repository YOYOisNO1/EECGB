def program2648():
    p1, p2 = input(), input()
    x1, y1 = ord(p1[0]) - ord('a') + 1, int(p1[1])
    x2, y2 = ord(p2[0]) - ord('a') + 1, int(p2[1])
    x = x2 - x1
    y = y2 - y1
    d1, d2 = 'L', 'D'
    # if x > 0:
    #     d1 = 'R'
    d1 = 'R' if x > 0 else x = -x
    # if y > 0:
    #     d2 = 'U'
    d2 = 'U' if y > 0 else y = -y
    # if x > y:
    #     print(x)
    # else:
    #     print(y)
    print(x) if x > y else print(y)
    # if x < 0:
    #     x = -x
    # if y < 0:
    #     y = -y
    while x or y:
        if x:
            x -= 1
            print(d1, end='')
        if y:
            y -= 1
            print(d2, end='')
        print()