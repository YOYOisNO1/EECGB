def program5262():
    #import numpy as np
    mod = 10 ** 9 + 7
    n, m, k = map(int, input().split())
    if k == 1 or k > n:
        print(pow(m, n, mod))
    elif k == n:
        print(pow(m, (n + 1) // 2, mod))
    else:
        print(pow(m, k % 2 + 1, mod))