def program1787():
    read = lambda: map(int, input().split())
    n, k = read()
    a = list(read())
    b = list(read())
    if k > 1:
        print('Yes')
    else:
        a[a.index(0)] = b[0]
        print('Yes' if a != sorted(a) else 'No')