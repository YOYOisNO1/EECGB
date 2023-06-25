def program1237():
    a, b, c = map(int, input().split())
    u = [a // 3, b // 2, c // 2]
    w = min(u)
    a -= w * 3
    b -= w * 2
    c -= w * 2
    ans = 0
    r = ['a', 'b', 'c', 'a', 'c', 'b', 'a', 'a', 'b', 'c', 'a', 'c', 'b', 'a']
    for i in range(7):
        a1 = a; b1 = b; c1 = c; k = 0
        for j in range(i, i + 7):
            if r[j] == 'a':
                a1 -= 1
            elif r[j] == 'b':
                b1 -= 1
            else:
                c1 -= 1
            if a1 < 0 or b1 < 0 or c1 < 0:
                break
            k += 1
        if k > ans:
            ans = k
    print(ans + w * 7)
        