def program975():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = b[0]
    b[0] = b[1]
    b[1] = b[2]
    b[2] = q
    Min = 0
    Max = 0
    for i in range(3):
        Min += max(a[i] - b[(i + 1) % 3] - b[(i + 2) % 3], 0)
        Max += min(a[i],b[i])
    print(Min, Max)