def program2581():
    n, a, b = map(int, input().split())
    for i in xrange(1, min(a, b) + 1):
        if a / i + b / i >= n:
            i += 1
        else:
            break
    print(i - 1)