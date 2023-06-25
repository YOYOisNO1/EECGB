def program5409():
    mod = 1000000007
    
    max_num = int(2e5) + 1
    
    factos = [0] * (max_num + 1)
    factos[0] = 1
    invs = [0] * (max_num + 1)
    cur = 1
    for i in range(1, max_num + 1):
        cur *= i
        cur %= mod
        factos[i] = cur
    
    invs[max_num] = pow(factos[max_num], mod - 2, mod)
    for i in range(max_num - 1, -1, -1):
        invs[i] = (i + 1) * invs[i + 1] % mod
    
    for _ in range(int(input())):
        n, k = map(int, input().split())
    
        if k == 0:
            print(1)
        else:
            if n % 2 == 0:
                contested = 0
                for i in range(0, n, 2):
                    contested += factos[n] * invs[i] * invs[n - i] % mod
                    contested %= mod
    
                dp = [0] * k
                dp[0] = contested + 1
    
                for i in range(1, k):
                    v = contested * dp[i - 1] + pow(2, n * i, mod)
                    v %= mod
                    dp[i] = v
            else:
                contested = 0
                for i in range(0, n, 2):
                    contested += factos[n] * invs[i] * invs[n - i] % mod
                    contested %= mod
                contested += 1
                contested %= mod
    
                dp = [0] * k
                dp[0] = contested
    
                for i in range(1, k):
                    v = contested * dp[i - 1]
                    v %= mod
                    dp[i] = v
    
            print(dp[-1])