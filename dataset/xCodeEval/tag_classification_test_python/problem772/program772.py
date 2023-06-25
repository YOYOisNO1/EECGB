def program772():
    t = int(input())
    for _ in range(t):
        x = int(input())
        a, b, c = map(int, input().split())
        d = {1: a, 2: b, 3: c}
        while len(d) > 0:
            if d[x] == 0 and len(d) > 1:
                print('NO')
                break
            y = d[x]
            del d[x]
            x = y
        else:
            print('YES')