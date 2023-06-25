def program2603():
    p = input()
    total = 0
    if p == 2:
        total = 1
    for x in range(2,p):
        cur = 1
        for y in range(1, p):
            cur *= x
            cur %= p
            if cur == 1 and y != p-1:
                break
            elif cur == 1 and y == p-1:
                total += 1
    print(total)