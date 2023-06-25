def program4041():
    inp = list(map(int, input().split()))
    a, b, c, d = inp
    inp.remove(d)
    inp.sort()
    a, b, c = inp
    if b-a>=d and c-b>=d:
        print(0)
    elif b-a>=d:
        print(d-c+b)
    elif c-b>=d:
        print(d-b+a)
    else:
        print(d-c+b+d-b+a)