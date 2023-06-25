    from functools import lru_cache
    
def extended_gcd(a, b):
        """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
        s, old_s = 0, 1
        r, old_r = b, a
        while r:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
        return old_r, old_s, (old_r - old_s * a) // b if b else 0
    
    @lru_cache(None)
def modinv(a, m):
        """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
        g, x, _ = extended_gcd(a % m, m)
        return x % m if g == 1 else None
    
def main():
        n, k = list(map(int, input().split(' ')))
        MOD = 998244353
        dp = [[[0] * n for _ in range(k + 1)] for _ in range(n)]
        dp_sum = [[0 for _ in range(k + 1)] for _ in range(n)]
        fpow = [[1 for _ in range(n)] for _ in range(k+1)]
        for i in range(k + 1):
            fpow[i][0] = 1
            for j in range(1, n):
                fpow[i][j] = fpow[i][j-1] * i % MOD
        for j in range(1,k+1):
            dp[0][j][1] = 1
            dp_sum[0][j] = 1
        for i in range(1, n-1):
            for j in range(1, k + 1):
                for num in range(1, i+1):
                    dp[i][j][num+1] = (dp[i-1][j][num] * fpow[k - j + 1][i] % MOD) * ((i+1) * modinv(num+1, MOD) % MOD) % MOD
                    dp_sum[i][j] = (dp_sum[i][j] + dp[i][j][num+1]) % MOD
                for z in range(1, j):  
                    dp[i][j][1] = (dp[i][j][1] + dp_sum[i-1][z] * fpow[k - j + 1][i] % MOD * (i+1)) % MOD
                dp_sum[i][j] = (dp_sum[i][j] + dp[i][j][1]) % MOD
    
        #print(dp)
        res = sum(dp_sum[n-2]) % MOD
        print(res)
                
        return
    
    main()