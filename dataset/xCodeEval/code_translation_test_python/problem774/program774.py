def program774():
    s = input()
    t = input()
    n_ins = len(t)
    current = 0
    for i in range(n_ins):
        if t[i] == s[current]:
            current += 1
    print(current) + 1