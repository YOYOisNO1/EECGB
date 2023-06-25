def program1370():
    a = []
    a.append(['X'] + list(input()) + ['X'])
    n = len(a[0])
    a.append(['X'] + list(input()) + ['X'])
    cnt = 0
    for i in range(1, n):
        #print(a[0][i])
        #print(a[1][i])
        if a[0][i] == '0' and a[1][i] == '0':
            if a[0][i-1] == '0':
                cnt += 1
                a[0][i-1] = 'X'
                a[0][i] = 'X'
                a[1][i] = 'X'
                continue
            elif a[1][i-1] == '0':
                cnt += 1
                a[1][i-1] = 'X'
                a[0][i] = 'X'
                a[1][i] = 'X'
                continue
            elif a[0][i+1] == '0':
                cnt += 1
                a[0][i+1] = 'X'
                a[0][i] = 'X'
                a[1][i] = 'X'
                continue
            elif a[1][i+1] == '0':
                cnt += 1
                a[1][i+1] = 'X'
                a[0][i] = 'X'
                a[1][i] = 'X'
                continue
    print(cnt)