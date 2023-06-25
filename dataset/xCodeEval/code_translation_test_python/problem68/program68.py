def program68():
    la = sorted(input().split())
    res = 2
    if int(la[0][0]) == int(la[1][0]) - 1 == int(la[2][0]) - 2:
        if la[0][1] == la[1][1] == la[2][1]:
            res = 0
        elif la[0][1] == la[1][1] or la[1][1] == la[2][1] or la[0][1] == la[2][1]:
            res = 1
    elif la[0][0] == la[1][0] == la[2][0]:
        if la[0][1] == la[1][1] == la[2][1]:
            res = 0
        elif la[0][1] == la[1][1] or la[1][1] == la[2][1] or la[0][1] == la[2][1]:
            res = 1
    else:
        if int(la[0][0]) == int(la[1][0]) - 2:
            if la[0][1] == la[1][1]:
                res = 1
        if int(la[1][0]) == int(la[2][0]) - 2:
            if la[1][1] == la[2][1]:
                res = 1
        if int(la[0][0]) == int(la[2][0]) - 2:
            if la[0][1] == la[2][1]:
                res = 1
        if int(la[0][0]) == int(la[2][0]) - 1:
            if la[0][1] == la[2][1]:
                res = 1
        if int(la[1][0]) == int(la[2][0]) - 1:
            if la[1][1] == la[2][1]:
                res = 1
        if int(la[0][0]) == int(la[1][0]) - 1:
            if la[0][1] == la[1][1]:
                res = 1
        if int(la[0][0]) == int(la[1][0]):
            if la[0][1] == la[1][1]:
                res = 1
        if int(la[1][0]) == int(la[2][0]):
            if la[1][1] == la[2][1]:
                res = 1
        if int(la[0][0]) == int(la[2][0]):
            if la[0][1] == la[2][1]:
                res = 1
    print(res)