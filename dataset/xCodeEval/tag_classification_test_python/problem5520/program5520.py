def program5520():
    s, v1, v2, t1, t2 = map(int, input().split())
    x1 = v1 * s + t1 * 2
    x2 = v2 * s + t2 * 2
    print("First") if x1 < x2 else "Second" if x2 < x1 else "Friendship"