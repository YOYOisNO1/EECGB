def solve(test):
        a, b, c, d = map(int, input().split())
        ans = min(a, c, d)
        a -= ans
        ans = 256 * ans + 32 * min(a, b)
        print(ans)
    t = 1
    for _ in range(t):
        solve(_ + 1)