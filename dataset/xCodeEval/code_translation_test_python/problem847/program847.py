def program847():
    a, b = map(int, input().split())
    aw, t, bw = 0, 0, 0
    for i in range(1, 7):
        if abs(a-i) < abs(b-i):
            aw += 1
        elif abs(a-i) > abs(b-i):
            bw += 1
        else:
            t += 1
    print(aw, t, bw)