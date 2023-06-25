def program5260():
    n, m, k = map(int, input().split())
    
    mod = 10 ** 9 + 7
    
    if k == 1 or k > n:
        print(pow(m, n, mod))
    elif k == n:
        print(pow(m, (n + 1) // 2, mod))
    else:
        print(pow(m, k % 2 + 1, mod))