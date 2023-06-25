def program5972():
    n = int(input())
    i, t = [0, 0]
    a, b = [1234567, 123456]
    while a * i <= n:
        j = 0
        while b * j + a * i <= n:
            if (n - a * i - b * j) % 1234 == 0:
                t = 1
                break
            j += 1
        i += 1
        if t: break
    if t: print('YES', end = '')
    else: print('NO', end = '')