def program2204():
    ﻿a, b = map(lambda x: int(x), input().split())
    k = 0
    while 1:
        a = a - b
        if a <= 0:
            break
        c = a
        k += 1
        s = 1
        while c != 1:
            s += c % 2
            c = c // 2
        if k - s == 1:
            s += 1
        if s == k:
            print(s)
            break
    
    if a <= 0:
        print(-1)