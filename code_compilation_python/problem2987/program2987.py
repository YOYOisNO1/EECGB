def program2987():
    n = int(input())
    a = list(map(int, input().split()))
    idx = []
    for i in range(1, n // 2 + 1):
        idx.append(2 * i + 1)
    a.sort()
    s1 = 0
    s2 = 0
    for i in range(0, n // 2):
        s1 += abs(a[i] - 2 * i -a 1)
        s2 += abs(a[i] - 2 * i - 2)
    print(min(s1, s2))