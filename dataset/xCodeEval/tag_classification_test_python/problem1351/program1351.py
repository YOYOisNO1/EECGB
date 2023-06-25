def program1351():
    n, m, k = map(int, input().split())
    m-=1
    arr = map(int, input().split())
    reverse = arr[::-1]
    dist = 1000000000
    for i in xrange(n):
        if arr[i] != 0 and arr[i] <= k:
            #rint abs(i - m)
            dist = min(dist, 10 * (abs(i - m)))
    print(dist)