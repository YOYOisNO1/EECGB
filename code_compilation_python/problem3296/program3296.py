def program3296():
    n = int(input())
    a = map(int, input().split(' '))
    m = max(a)
    m1 = min(a)
    i = a.index(m)
    a[i], a[0] = a[0], a[i]
    i = a.index(m1)
    a[i], a[n - 1] = a[n - 1], a[i]
    a = a[1:n - 1]
    a.sort()
    print m,
    for i in range(n - 2):
        print a[i],
    print m1,