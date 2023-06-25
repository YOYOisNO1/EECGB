def program2784():
    n = int(input())
    a = list(map(int, input().split()))
    ans = True
    an = []
    c = 0
    for i in range(len(a)):
        if a[i] != 0:
            an.append([c + 1, i + 1])
            c = i + 1
    if len(an) and a[-1] == 0:
        h = an.pop()
        an.append([h[0], n])
    if len(an):
        print("YES")
        print(len(an))
        for e in an:
            print(*e)
    else:
        print("NO")