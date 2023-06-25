def program2988():
    n = input()
    P = sorted(map(int, input().split()))
    e = sum(abs(p - 1 - 2 * i) for i, p in enumerate(P))
    o = sum(abs(p - 1 - (2 * i + 1) for i, p in enumerate(P))
    print(min(e, o))