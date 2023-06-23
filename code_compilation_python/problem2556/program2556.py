def program2556():
    t, m = input(), input()
    n, d = int(t), len(t)
    s, p = 0, 1
    j = len(m)
    while j:
        i = max(0, j - d)
        k = int(m[i: j])
        if k >= n:
            i += 1
            k = int(m[i: j])
        while m[i] == '0': i += 1
        j = i
        s += k * p
        p *= n
    print(s)