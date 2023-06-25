def program722():
    k, b, n, t = map(int, input().split())
    if k == 1:
        print(max(0, (n * b - t + b) // b))
    else:
        x, y, v = k - 1 + b, t * (k - 1) + b, 0
        while x * k <= y:
            x *= k
            v += 1
        print(max(0, n - v))