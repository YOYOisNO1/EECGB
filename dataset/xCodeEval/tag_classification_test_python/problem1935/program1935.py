def program1935():
    n = int(input())
    s = str(n)
    r = n - 9 * len(s)
    k = []
    if r < 0:
        r = 0
    for i in range(r, n + 1):
        ls = str(i)
        x = i
        for y in ls:
            x += int(y)
        if x == n:
            k.append(i)
    if k:
        print(len(k))
        for i in k:
            print(i)
    else:
        print(0)
    
    