def program1277():
    (k2, k3, k5, k6) =list(map(int, input().split()))
    min256 = min((k2, k5, k6))
    min32 = min((k2-min256, k3))
    if min32 < 0:
        min32 = 0
    print(min256) * 256 + min32 * 32