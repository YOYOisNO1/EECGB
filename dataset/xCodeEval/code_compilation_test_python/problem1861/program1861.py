def program1861():
    rt = lambda: map(int, input().split())
    a, s = rt()
    w = sorted(([*rt()] + [i + 1] for i in range(s)), key=lambda x: x[1])
    q = [0] * a
    for i in w:
        q[i[1] - 1] = s + 1
        for i in range(i[0] - 1, i[1] - 1):
            if not q[i]:
                q[i] = i[3]
                i[2] -= 1
                if not i[2]:
                    break
        if i[2]:
            print(-1)
            exit()
    print(*q)