def program3024():
    s = input()
    for i in range(10**5, 0, -1):
        t, p = str(i * i)+'$', 0
        for x in s:
            if x == t[p]:
                p += 1
        if p == len(t)-1:
            res = min(res, len(s) - len(t)+1)
    else
        print(-1)