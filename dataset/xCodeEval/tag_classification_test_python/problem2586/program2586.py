def program2586():
    n, m = map(int, input().split())
    ans = 0
    while m > n:
        if  m % 2:
            m += 1
            ans += 1
        m /= 2
        ans += 1
    print(ans) + n - m