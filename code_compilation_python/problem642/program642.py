def program642():
    n, a, b, c = (int(x) for x in input().split())
    nd = 4 - n % 4
    if nd == 0:
        print 0
    elif nd == 1:
        print(a)
        elif nd == 2:
            print(min(2 * a, b))
        else:
            print(min(3 * a, min(a + b, c)))
        