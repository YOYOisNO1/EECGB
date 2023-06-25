def program489():
    n, k = map(int, input().split())
    s = input()
    g = s.index('G'); t = s.index('T')
    dis = g-t
    if abs(dis) % k == 0 and dis < 0:
        for i in range(g, t+1, k):
            if s[i] == '#':
                print('NO')
                exit()
    elif dis % k == 0 and dis >= 0:
        for i in range(t, g+1, k):
            if s[i] == '#':
                print('NO')
                exit()
    else:
        print('NO')
        exit()
    print('YES')