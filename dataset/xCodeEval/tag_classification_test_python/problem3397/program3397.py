def program3397():
    s, m = 0, 0
    for i in range(8):
        t = input()
        if t == 'BBBBBBBB': s += 1
        else: m = max(m, t.count('B'))
    print(s + m)