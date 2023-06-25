def program1236():
    x, y, z, t1, t2, t3 = map(int, input().split())
    a1 = abs(x - y) * t1
    a2 = abs(x - z) * t2 + t3 * 3 + abs(x - y) * t2
    if a1 < a2:
        print("NO")
    else:
        print("YES")