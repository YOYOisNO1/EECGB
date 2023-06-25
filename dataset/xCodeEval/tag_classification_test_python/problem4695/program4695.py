def program4695():
    read = lambda: map(int, input().split())
    n, k = read()
    s = input()
    ev = []
    for i in range(26):
        c = chr(ord('A') + i)
        if s.count(c):
            l = s.find(c)
            r = s.rfind(c)
            ev.append((l, 1))
            ev.append((r, -1))
    ev.sort(key = lambda x: (x[0], -x[1]))
    bal = 0
    flag = 0
    for x, t in ev:
        bal += t
        if bal > k:
            flag = 1
            break
    print('YES' if flag else 'NO')