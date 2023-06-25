def program2476():
    n = input()
    if n == '1': print(1)
    else:
        t, y, x = [], set(n), int(n)
        for d in range(2, int(x ** 0.5) + 1):
            if x % d == 0: t += [d, x // d]
        if t[-1] == t[-2]: t.pop()
        print(1 + int('1' in y) + sum(len(set(str(i)) & y) > 0 for i in t))