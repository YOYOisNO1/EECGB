def program608():
    n, m, a = map(int, input().split())
    if n and m > a:
        print((n // a + 1) * 2)
    elif:
        n > a and m <= a:
            print((n // a) * 2)
    elif:
        m > a and n <= a:
            print((m // a) * 2)
    else:
        print(m * n // (a * a))