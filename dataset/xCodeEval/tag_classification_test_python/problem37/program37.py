def program37():
    a, b, c, d = map(int, input().split())
    if a + b == c + d:
        print('YES')
    elif a + c == b + d:
        print('YES')
    elif a + d == b + c:
        print('YES')
    elif a + b + c == d:
        print('YES')
    elif b + c + d == a:
        print('YES')
    elif c + d + a == b:
        print('YES')
    elif d + a + b == c:
        print('YES')
    else:
        print('NO')