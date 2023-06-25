    from functools import lru_cache
    import io
    import os
    
    FILE_INPUT_MODE = 0  # 0 for BytesIO, 1 for input.txt, -1 for stdin, input()
    if FILE_INPUT_MODE >= 0:
    
        if FILE_INPUT_MODE == 1:
            CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
            FD = os.open(f"{CURRENT_DIR}\input.txt", os.O_RDONLY)
        elif FILE_INPUT_MODE == 0:
            FD = 0
        DATA = io.BytesIO(os.read(FD, os.fstat(FD).st_size))
        if FD != 0:
            os.close(FD)
    
    def input():
            return DATA.readline().decode().rstrip('\r\n')
    
    p = 998244353
    
    
    @lru_cache(None)
def inv(x):
        return pow(x, p - 2, p)
    
    
    @lru_cache(None)
def fact(x):
        if x <= 1:
            return 1
        return x * fact(x - 1) % p
    
    
def comb(x, y):
        return fact(x) * inv(fact(y)) * inv(fact(x - y)) % p
    
    
def solve():
        n, k = [int(word) for word in input().strip().split()]
        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
        s = [[0 for j in range(k + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                dp[1][0] = 1
            elif i == 2:
                for j in range(1, k + 1):
                    dp[2][j] = 1
            else:
                for x in range(1, i):
                    cnt = x * (x - 1) // 2 + (i - 1 - x) * x
                    for j in range(k, 0, -1):
                        dp[i][j] += s[i - x][j - 1] * \
                            comb(i - 1, x) * pow(k - j + 1, cnt, p) % p
                        dp[i][j] %= p
            s[i][0] = dp[i][0]
            for j in range(1, k + 1):
                s[i][j] = (s[i][j - 1] + dp[i][j]) % p
        return s[n][k]
    
    
def main():
        print(solve())
    
    
    if __name__ == "__main__":
        main()