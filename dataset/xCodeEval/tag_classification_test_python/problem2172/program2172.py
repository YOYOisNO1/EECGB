def program2172():
    x, y, z, t1, t2, t3 = list(map(int, input().split()))
    if (abs(x - z) + abs(x - y)) * t2 + (3 * t3) <= t1 * abs(x - y):
        print("YES")
    else:
        print("NO")