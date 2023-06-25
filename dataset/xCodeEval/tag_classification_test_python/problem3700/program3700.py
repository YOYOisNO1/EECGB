def program3700():
    text = input()
    rez = 0
    for i in range(len(text)):
        zd = i * '0' + text
        if zd == zd[::-1]:
            rez = 1
            break
    print('YES' if rez else 'NO')