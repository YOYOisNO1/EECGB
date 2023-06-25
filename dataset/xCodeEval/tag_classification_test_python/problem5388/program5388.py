    import sys
    
    readline = sys.stdin.readline
    
    M = 10**9 + 7
    
def bin_exp(num, k):
        ans = 1
        num %= M
        while k > 0:
            if k % 2 == 1:
                ans *= num
                ans %= M
            num *= num
            num %= M
            k //= 2
        return ans
    
    t = int(readline())
    for _ in range(t):
        n, k = map(int, readline().split())
        if k == 0:
            print(1)
            continue
        two_n_1 = bin_exp(2, n-1)
        if n%2 == 1:
            two_n_1 = (two_n_1 + 1) % M
            print(bin_exp(two_n_1, k) % M)
        else:
            dp = [0]* k
            dp[0] = two_n_1
            two_n = (2* two_n_1) % M
            two_n_1 -= 1
            if two_n_1 < 0: 
                two_n_1 += M
            two_n_k = 1
            for i in range(1, k):
                dp[i] = (dp[i-1] * two_n_1) % M
                two_n_k *= two_n
                two_n_k %= M
                dp[i] += two_n_k
                dp[i] %= M
            print(dp[k-1] % M)