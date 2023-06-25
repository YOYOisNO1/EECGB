def program1930():
    n = int(input())
    m = 'abcdefghijklmnopqrstuvwxyz'
    stroka = input().lower()[:n + 1]
    not_found = False
    for i in range(len(m)):
        if m[i] not in stroka:
            not_found = True
            break
    if not_found is True:
        print('NO')
    else:
        print('YES')