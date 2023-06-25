def program1724():
    h, n = map(int, input().split())
    N = bin(n - 1)[2:]
    N = '0' * (h - len(N)) + N
    ans = 0
    f = False
    for i in range(h):
        if N[i] != ('1' if not f else '0'):
            f = not f
            ans += 1
        else:
            ans += 2 ** (h - i)
    print(ans)