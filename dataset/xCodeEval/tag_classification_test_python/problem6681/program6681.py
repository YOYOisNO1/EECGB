def program6681():
    s1, s2, t1, t2 = [input() for _ in range(4)]
    a = [s1[0], s1[1], s2[1], s2[0]]
    b = [t1[0], t1[1], t2[1], t2[0]]
    a.pop(a.index('X'))
    b.pop(b.index('X'))
    ai = a.index('A')
    bi = b.index('A')
    for i in 'ABC':
        if a[ai] != b[bi]:
            print('NO')
            exit()
        ai = (ai + 1) % 3
        bi = (bi + 1) % 3
    print('YES')