def program325():
    n, k = list(map(int, input().split()))
    check = False
    while True:
        for i in range(1, 10):
            f = i * (10 ** k)
            if f % n == 0:
                check = True
                break
        if check:
            break
    print(f)