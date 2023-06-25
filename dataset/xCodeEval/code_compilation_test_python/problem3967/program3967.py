def program3967():
    l = map(int, input().split())
    n = l[0]
    k = l[1]
    x = long(pow(n-k, n-k, 10**9+7))
    y = long(pow(2, (k*(k-1))/2, 10**9+7))
    print (x*y) % (10**9+7)