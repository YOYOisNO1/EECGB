def program2652():
    a = [1200, 1400, 1600, 1900, 2100, 2300, 2400, 2600, 3000]
    r = int(input())
    for i in a:
        if i > r:
            print(i)
            return