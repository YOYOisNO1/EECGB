def program56():
    a, b = map(int, input().split())
    ans = 1
    for i in range(a + 1, min(b + 1, a + 20)):
        ans *= i
        ans %= 10
    print(ans)