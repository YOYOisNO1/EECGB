def solve(n, x, y):
        if(x == 0):
            return y
        elif y == n:
            return y + x
        elif x == n:
            return 3 * m - y
        else:
            return 4 * n - x
    
    n, x1, y1, x2, y2 = map(int, input().split(" "))
    p1 = solve(n, x1, y1)
    p2 = solve(n, x2, y2)
    
    print min((p1 - p2 + 4 * n) % (4 * n),(p2 - p1 + 4 * n) % (4 * n)