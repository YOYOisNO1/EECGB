def program1552():
    s = 0
    for i in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        a1, b1, a2, b2 = min(a1, x1), min(b1, y1), max(a2, x2), max(b2, y2)
        s += (x2 - x1) * (y2 - y1)
    print('YES' if s == (a2 - a1) * (b2 - b1) else 'NO')