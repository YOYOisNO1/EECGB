def program2823():
    input()
    n = [int(x) for x in input().split()]
    a = -1
    aa = 0
    for i, x in enumerate(n):
        aaa = aa + len([x in n[i:] if x])
        if aaa > a:
            a = aaa
        if not x:
            aa += 1
    print(max(a,aa))