def program2230():
    read = lambda: map(int, input().split())
    a, b, c = read()
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    k = gcd(a, b)
    a //= k
    b //= k
    x = str(a/b)
    ans = -1
    for i in range(2, min(12, len(x))):
        if int(x[i]) == c:
            ans = i - 1
            break
    if ans == -1 and c == 0 and len(x) < 12:
        ans = len(x) - 1
    print(ans)