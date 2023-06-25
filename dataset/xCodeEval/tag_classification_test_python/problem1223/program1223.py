def program1223():
    n = int(input())
    i, t = 2, [1]
    while i * i < n + 1:
        while n % i == 0:
            t.append(i)
            n //= i
        i += 1
    if n > 1: t.append(n)
    for i in range(1, len(t)):
        t[i] = t[i - 1] * t[i]
    t.reverse()
    print(' '.join(str(i) for i in t))