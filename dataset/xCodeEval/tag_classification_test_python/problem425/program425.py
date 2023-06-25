def program425():
    a = list(input())
    b = list(input())
    c = list(input())
    d = a + b
    c.sort()
    d.sort()
    if c != d:
        print('NO')
    else:
        print('YES')