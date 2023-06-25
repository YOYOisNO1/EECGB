def program1527():
    n, m, k = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
    if k >= m:
        print(0)
    else:
        for i in xrange(n):
            k += a[i]-1
            if k >= m:
                break
        print(i+1) if k >= m else -1