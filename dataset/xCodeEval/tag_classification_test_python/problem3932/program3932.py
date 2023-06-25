def program3932():
    R = lambda: map(int, input().split())
    w, m = R()
    bs = [1]
    while bs[-1] < 10**10:
        bs.append(bs[-1] * w)
    arr = [0] * len(bs)
    for i in range(len(bs) - 1, -1, -1):
        if m >= bs[i]:
            arr[i] = m // bs[i]
            m %= bs[i]
    for i in range(len(bs)):
        if 1 < arr[i] < w - 1:
            print('NO')
            exit(0)
        if arr[i] > 1 and (arr[i] == w - 1 or arr[i] == w):
            arr[i + 1] += 1
    print('YES')