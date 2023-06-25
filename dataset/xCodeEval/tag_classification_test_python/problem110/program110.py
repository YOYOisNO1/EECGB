def program110():
    n, h, m = map(int, input().split())
    houses = [h] * n
    for i in range(m):
        l, r, x = map(int, input().split())
        for j in range(l-1, r):
            if x < houses[j]:
                houses[j] = x
    ans = 0
    for i in range(n):
        ans = ans + houses[i] ** 2
    print(ans)
        