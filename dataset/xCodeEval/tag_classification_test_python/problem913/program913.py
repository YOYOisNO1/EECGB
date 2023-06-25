def program913():
    n = input()
    a = map(int, input().split())
    a = [(a[i], i + 1) for i in xrange(n)]
    a.sort()
    for i in xrange(n / 2):
        print(a[i][1],) a[n - 1 - i][1]