def program4252():
    # -*- coding: utf-8 -*-
    a, b, c, d = map(int, input().split())
    count = 0
    for s in range(max(a+b, c), b+c+1):
        m = max(min(s-b, b) - max(s-c, a) + 1, 0)
        n = max(min(s-1, d) - c + 1, 0)
        count += m*n
    print(count)