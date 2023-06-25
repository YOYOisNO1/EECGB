def program6330():
    n = input()
    t = int(int(n) ** 0.5)
    while t > 0:
        m = str(t * t)
        j = 0
        for i in range(len(n)):
            if n[i] == m[j]:
                j += 1
                if j == len(m):
                    print(len(n) - j)
                    exit()
        t -= 1
    print('-1')