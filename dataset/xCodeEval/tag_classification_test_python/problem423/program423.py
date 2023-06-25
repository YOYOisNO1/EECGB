def program423():
    guest = input()
    host = input()
    combine = guest + host
    z = input()
    p = 1
    for i in z:
        if z.count(i) != combine.count(i):
            p = 0
    for i in combine:
        if z.count(i) != combine.count(i):
            p = 0
    if p:
        print('YES')
    else:
        print('NO')