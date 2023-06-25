def program1760():
    f = list(map(int, input().split()))
    w = f[0]
    h = f[1]
    n = f[2]
    s = 0
    d = 2
    for i in range(n):
    s = s + (w + h - d)*2
    d = d + 8
    print(s)