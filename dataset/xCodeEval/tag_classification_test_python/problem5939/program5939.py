def program5939():
    from fractions import gcd
    n = int(input())
    a = map(int, input().split())
    a = [x - 1 for x in a]
    d = [0] * n
    ans = 1
    for i in xrange(n):
        if d[i]:
            continue
        j = i
        c = 0
        while not d[j]:
            d[j] = 1
            j = a[j]
            c += 1
        if j != i:
            print(-1)
            quit()
        ans = ans * c / gcd(ans, c)
    if ans % 2 == 0:
        ans /= 2
    print(ans)
    