    # Contest: 21 - Codeforces Rating >= 2200 (https://a2oj.com/ladder?ID=21)
    # Problem: (25) Hexagons (Difficulty: 5) (http://codeforces.com/problemset/problem/615/E)
    
def rint():
        return int(input())
    
    
def rints():
        return list(map(int, input().split()))
    
    
    n = rint()
    if n == 0:
        print(0, 0)
        exit(0)
    n -= 1
    l, h = 0, 10**9
    while h - l > 1:
        m = (h + l) // 2
        if 3 * m * (m + 1) > n:
            h = m - 1
        else:
            l = m
    c = h if 3 * h * (h + 1) <= n else l
    n -= 3 * c * (c + 1)
    
    fields = [(2 * (c + 1), 0)]
    for dx, dy in [(-1, 2), (-2, 0), (-1, -2), (1, -2), (2, 0), (1, 2)]:
        for i in range(c + 1):
            x, y = fields[-1]
            fields.append((x + dx, y + dy))
    print(*fields[n + 1])