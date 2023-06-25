def program147():
    n, m = map(int, input().split())
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    a = "NO"
    while True:
        n += 1
        if n in p:
            if n == m:
                a = "YES"
                break
            else:
                break
        if n > m:
            break
    print(a)