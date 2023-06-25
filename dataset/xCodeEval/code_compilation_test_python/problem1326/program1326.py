def program1326():
    n, v = map(int, input().split())
    if v >= n:
        print(min(v,n)
    else:
        cost = v
        d = n - v - 1
        cost += d + d * (d + 1) // 2
        print(cost)