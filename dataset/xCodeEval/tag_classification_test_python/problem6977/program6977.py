def C(n, k):
        if k == 3:
            return n * (n - 1) * (n - 2) // 6
        else:
            return n * (n - 1) // 2
    
    
    ss = input().split()
    n = int(ss[0])
    p = float(ss[1])
    for k in range(n + 1):
        cur = C(n - k, 3) / C(n, 3) + ((1/3) + (1/3) * (1/2)) * k * C(n - k, 2) / C(n, 3)
        if 1 - cur >= p:
            print(k)
            break