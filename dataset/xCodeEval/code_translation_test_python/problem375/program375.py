def program375():
    a1 = int(input())
    a2 = int(input())
    k1 = int(input())
    k2 = int(input())
    n = int(input())
    if k1 > k2:
        k1, k2 = k2, k1
        a1, a2 = a2, a1
    ans1 = 0
    if n // k1 > a1:
        ans1 = a1 + min((n - a1 * k1) // k2, a2)
    else:
        ans1 = n // k1
    ans2 = 0
    n -= a1 * (k1 - 1)
    n -= a2 * (k2 - 1)
    ans2 = max(n, 0)
    print(ans2, ans1)