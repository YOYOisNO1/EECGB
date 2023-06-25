def program2678():
    a = list(map(int,input().split()))
    i = a[0]
    j = a[1]
    k = a[2]
    print((min(2) * i + 2 * j, min(i + j + k, min(j * 2 + k * 2, i * 2 + k * 2))))