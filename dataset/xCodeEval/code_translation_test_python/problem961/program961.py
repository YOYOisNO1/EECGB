def program961():
    n,k = [int(i) for i in input().split()]
    ans = 0
    for i in range(k):
        if n >= 2:
            ans +=  2 * n  - 3
            n -= 2
    print(ans)