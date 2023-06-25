def program27():
    n, k, t = map(int, input().split())
    ans = t
    if t > k:
        ans = k
    if t > n:
        ans -= (t-n)
    print(ans)