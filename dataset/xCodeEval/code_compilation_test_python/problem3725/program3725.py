def program3725():
    ﻿n = int(input())
    a = []
    while n > 0:
        n -= 1
        a.append(1)
        while len(a) > 1 and a[-1] == a[-2]:
            a[-2] = a[-2] + 1
            a.pop()
    for e in a:
        print(e, end=' ')