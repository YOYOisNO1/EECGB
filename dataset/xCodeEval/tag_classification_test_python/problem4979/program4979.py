    import time
    
    mod = int(1e9 + 7)
    
def fast_expo(x, k):
        ans = 1
        while k > 0:
            if (k & 1) > 0:
                ans = (ans * x) % mod
            x = (x * x) % mod
            k >>= 1
        return ans
    
def inverse(x):
        return fast_expo(x, mod - 2)
    
    N, K = [int(_) for _ in input().split()]
    start_time = time.time()
    prime_factors = {}
    i = 2
    curr = N
    while i * i <= curr:
        if curr % i == 0:
            prime_factors[i] = 0
            while curr % i == 0:
                prime_factors[i] += 1
                curr //= i
        i += 1
    
    if curr > 1:
        prime_factors[curr] = 1
    # print(time.time() - start_time)
    
    inv = {i: inverse(i) for i in range(60)}
    
    ans = 1
    for p in prime_factors:
        size = prime_factors[p]
        dp = [0] * (size + 1)
        dp[0] = 1
        pre = [1] * (size + 1)
        for e in range(1, size + 1):
            dp[e] = (p * dp[e - 1]) % mod
            pre[e] = (pre[e - 1] + dp[e]) % mod
        for it in range(K):
            # print(dp, pre)
            dpNext = [0] * (size + 1)
            preNext = [1] * (size + 1)
            for e in range(1, size + 1):
                dpNext[e] = (inv[e + 1] * pre[e]) % mod
                preNext[e] = (preNext[e - 1] + dpNext[e]) % mod
            dp = dpNext
            pre = preNext
        ans = (ans * dp[size]) % mod
    
    # print(time.time() - start_time)
    # because the dp is multiplicative, we can merge the answer
    print(ans)