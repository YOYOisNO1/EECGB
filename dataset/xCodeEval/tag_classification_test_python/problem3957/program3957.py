def program3957():
    w, m = map(int, input().split())
    p = 1
    for i in range(100):
        if m == 0: break
        if (m - p) % (p*w) == 0: m -= p
        elif (m + p) % (p*w) == 0: m += p
        p *= w
    if m == 0:
        print("YES")
    else:
        print("NO")