def program2579():
    n, a, b = map(int, input().split())
    mn = min(a, b)
    mx = a + b - mn
    for i in range(mn, 0, -1):
        if n == mn // i:
            if mx >= mn // (n - 1):
                print(i)
                exit(0)
        elif mx // (n - (mn // i)) >= i:
            print(i)
            exit(0)
    print(1)