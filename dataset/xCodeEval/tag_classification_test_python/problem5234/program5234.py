def program5234():
    n = int(input())
    s = [int(x) for x in input().split()]
    b = []
    c = []
    for i in s:
        if i > 0:
            b.append(i)
        else:
            c.append(i)
    print(sum(b) - sum(c))