def program1645():
    n, k = map(int, input().split())
    
    if k % 2 == 1:
        z = (k - 1) // 2
        if z > n:
            print(0)
        else:
            print(min(z, abs(n - z)))
    else:
        z = k // 2
        if z >= n:
            print(0)
        else:
            print(min(n - z, z - 1))
    