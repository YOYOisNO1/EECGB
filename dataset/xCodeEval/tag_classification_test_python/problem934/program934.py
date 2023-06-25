def program934():
    n, a, b = map(int, input().split())
    if a > b:
        a, b,  = b, a
    cur = list(range(1, n + 1))
    c = 1
    while len(cur) > 2:
        new = []
        for i in range(0, len(cur), 2):
            if i == len(cur) - 1:
                new += [cur[i]]
                break
            if cur[i] == a and cur[i + 1] == b:
                print(c)
                exit(0)
            if cur[i] == a or cur[i] == b:
                new += [cur[i]]
            else:
                new += [cur[i + 1]]
        c += 1
        cur = new[::]
    print('Final!')