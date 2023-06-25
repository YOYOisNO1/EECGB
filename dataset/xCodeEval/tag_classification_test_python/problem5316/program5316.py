def program5316():
    n, m = map(int, input().split())
    c = [0]*n + [1] + [0]*n
    for i in range(n-1, 0, -1):
        c[i] = 2*c[i+1] % m
        for j in range(2, n//i + 1):
            c[i] = (c[i] + c[i*j] - c[(i+1)*j]) % m
     
    print((c[1] - c[2]) % m)