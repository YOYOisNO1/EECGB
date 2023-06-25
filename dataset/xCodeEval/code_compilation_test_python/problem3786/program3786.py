def program3786():
    a = input()
    b = ''
    if a[0] + a[1] + a[2] == 'dot':
        b += 'dot'
        i = 3
    elif a[0] + a[1] == 'at':
        b += at
        i = 2
    else:
        i = 0
    at = 0
    while i < len(a) - 3:
        if a[i] == 'd' and a[i + 1] == 'o' and a[i + 2] == 't':
            b += '.'
            i += 3
        elif a[i] == 'a' and a[i + 1] == 't' and at == 0:
            b += '@'
            at = 1
            i += 2
        else:
            b += a[i]
            i += 1
    if a[i] + a[-1] == 'at' and at == 0:
        b += '@'
        b += a[i + 2]
    else:
        for j in range(i, len(a)):
            b += a[j]
    print(b)