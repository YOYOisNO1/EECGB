def program3021():
    u, v = map(int, input().split())
    if u > v:
        print((-1))
    elif u == 0 and v == 0:
        print((0))
    elif u == v:
        print((1))
        print((u))
    elif (v-u) % 2 == 0:
        d = (v-u) // 2
        if (u+d) ^ d == u:
            print((2))
            print((u+d,) d)
        else:
            print((3))
            print((u,) d, d)
    else:
        print((-1))