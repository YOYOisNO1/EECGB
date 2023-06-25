def program141():
    n = int(input())
    a = list(map(int, input().split()))
    rec = []
    for i in range(n):
        if a[i] != 5:
            rec.append((a[i], i))
    rec = sorted(rec)
    j = 0
    s = sum(a)
    while s < 4.5 * n:
        s += 5 - a[rec[j][1]]
        j += 1
    print(j)