def program3369():
    n = int(input())
    wyn = 0
    x = 1
    while True:
        if x * x > n:
            break
        if n%x == 0:
            if x*x != n:
                wyn += 2
            else:
                wyn += 1
        x += 1
    print(wyn)