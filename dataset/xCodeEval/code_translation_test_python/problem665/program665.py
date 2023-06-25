def program665():
    a, b = sorted(map(int, input().split()))
    ans = 0
    while a > 0 and b > 1:
        a += 1
        b -= 2
        a, b = sorted([a, b])
        ans += 1
    print(ans)