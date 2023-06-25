def program4853():
    import sys
    a,b = [int(n) for n in input().split()]
    x = 1
    c = 0
    if a == b:
        print('infinity')
        sys.exit(0)
    while x ** 2 <= a - b:
        if (a-b) % x == 0:
            if x > b:
                c += 1
            if x ** 2 != a - b and (a-b) / x > b:
                c += 1
        x += 1
    print(c)