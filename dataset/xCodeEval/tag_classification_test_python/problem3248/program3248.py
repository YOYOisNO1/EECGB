def program3248():
    x0, y0, ax, ay, bx, by = list(map(int, input().split()))
    xs, ys, t = list(map(int, input().split()))
    
    nodes = [(x0, y0)]
    x, y = x0, y0
    for i in range(99):
        x = x * ax + bx
        y = y * ay + by
        nodes.append((x, y))
    
    
    best = 0
    for i in range(100):
        ti = t
        x, y = xs, ys
        cnt = 0
        for j in range(i, 100):
            xj, yj = nodes[j]
            ti -= abs(xj - x) + abs(yj - y)
            if ti < 0:
                break
            cnt += 1
            x, y = xj, yj
        best = max(best, cnt)
    
        ti = t
        x, y = xs, ys
        cnt = 0
        for j in range(i, -1, -1):
            xj, yj = nodes[j]
            ti -= abs(xj - x) + abs(yj - y)
            if ti < 0:
                break
            cnt += 1
            x, y = xj, yj
        best = max(best, cnt)
    print(best)