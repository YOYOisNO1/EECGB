def program1097():
    n = int(input())
    r1, s1, p1 = map(int, input().split())
    r2, s2, p2 = map(int, input().split())
    max_win = min(r1, s2) + min(s1, p2) + min(p1, r2)
    min_win = max(s1 - r2 - s2, p1 - p2 - s2, r1 - r2 - p2, 0)
    print(min_win, max_win)