def program38():
    from sys import stdin
    a1,a2,a3,a4 = map(int, stdin.readline().rstrip().split(' '))
    
    if a1 + a2 == a3 + a4:
        print('YES')
    elif a1 + a3 == a2 + a4:
        print('YES')
    elif a1 + a4 == a2 + a3:
        print('YES')
    elif a1 + a2 + a3 == a4:
        print('YES')
    elif a2 + a3 + a4 == a1:
        print('YES')
    elif a1 + a2 + a4 == a3:
        print('YES')
    elif a1 + a3 + a4 == a2:
        print('YES')
    else:
        print('NO')