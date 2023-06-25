def program4792():
    n, m = (int(x) for x in input().split())
    ans = 0
    a = []
    for i in range(n):
        a.append(input())
        if 'S' not in a[i]:
            ans += m
    ans0 = ans
    for i in range(m):
        k = 0
        for j in range(n):
            if a[j][i] == 'S':
                k = 1
        if k == 0:
            ans0 += n - ans // m
    print(ans0)