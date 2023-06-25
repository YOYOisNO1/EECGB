def program1720():
    input()
    d1 = [int(x) for x in input().split()]
    s = set()
    d2 = []
    for x in reversed(d1):
        if x not in s:
            s.add(x)
            d2.append(x)
    print(len(d2))
    print(' '.join(map(str, reversed(d2))))