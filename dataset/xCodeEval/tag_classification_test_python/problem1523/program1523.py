def program1523():
    n, m, k = map(int, input().split())
    a = map(int, input().split())
    if sum(a) + k - n < m:
        print(-1)
        exit()
    
    a.sort(reverse = True)
    a.insert(0, 1)
    for i in xrange(n + 1):
        k += a[i] - 1
        if k >= m:
            print(i)
            exit()