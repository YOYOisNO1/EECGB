def program2540():
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    r = -1
    n -= 1
    for i in range(m - n):
    	if a[i + n] - a[i] < r or r == -1: r = a[i + n] - a[i]
    print(r)