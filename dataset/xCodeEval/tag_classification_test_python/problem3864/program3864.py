def program3864():
    n, k = map(int, input().split())
    l = []
    s = input()
    for i in s:
        l.append(i)
    mn = set(s)
    for i in mn:
        r = l.count(i)
        if k % r == 0:
            continue
        elif k % r != 0 and k<r:
            print('NO')
            break
    else:
        print('YES')