def program3799():
    ﻿a, b = map(int, input().split())
    aest = list(map(int, input().split()))
    best = set(aest)
    maxim = 0
    for i in best:
        if maxim < aest.count(i):
            maxim = aest.count(i)
    colvo = (maxim + b - 1) // b
    print(len(best) * colvo * b - a)