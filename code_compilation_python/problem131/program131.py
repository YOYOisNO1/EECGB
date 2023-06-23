def program131():
    k = int(input())
    if k % 2 == 0:
        if k / 2 > 17:
            print(-1)
        else:
            print('8' * (k // 2))
    else:
        if k / 2 + 1 > 17:
            print(-1)
        else:
            print('8' * (k // 2), '9', sep = '')