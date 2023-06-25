def program3968():
    n, m = [int(x) for x in input().split()]
    balans = m
    if n == 2 or m == 1:
        print('YES')
        exit()
    cur = 1
    while True:
        cur2 = cur * n
        if balans % cur2 == cur:
            balans -= cur
        elif balans % cur2 == cur2 - cur:
            balans += cur
        elif balans % cur2 == 0:
            balans += 0
        else:
            print('NO')
            exit()
        if balans == 0:
            print('YES')
            exit()
        cur = cur2