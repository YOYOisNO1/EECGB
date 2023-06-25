def program890():
    n = input()
    a = list(map(int, input().split()))
    total = 0
    
    f = [
        [],
        [0, 0, 3, 4],
        [0, 3, 0, 0],
        [0, 4, 0, 0]
    ]
    
    ok = True
    for a1, a2 in zip(a, a[1:]):
        x = f[a1][a2]
        if x == 0:
            ok = False
            break
        total += x
    if ok:
        total -= sum(1 for x, y, z in zip(a, a[1:], a[2:]) if x == 3 and y == 1 and z == 2)
    print('Finite\n{}'.format(total) if ok else 'Infinite')