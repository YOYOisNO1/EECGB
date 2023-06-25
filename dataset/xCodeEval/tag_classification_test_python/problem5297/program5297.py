    # template begins
    #####################################
    from io import BytesIO, IOBase
    import sys
    import math
    import os
    import heapq
    from collections import defaultdict, deque
    from math import ceil
    from bisect import bisect_left, bisect_left
    from time import perf_counter
    
    
    # region fastio
    
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
    def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
    
    def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
    
    def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()
    
    def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)
    
    
    class IOWrapper(IOBase):
    def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    
    
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")
def mint(): return map(int, input().split())
def mfloat(): return map(float, input().split())
def intin(): return int(input())
    
    
    #####################################
    # template ends
    # Use the recursion snippet if heavy recursion is needed (depth>1000)
    # If constraints are tight, use 1d arrays instead of 2d, like g[i*m+j] instead of g[i][j]
def solve():
        n, mod = map(int, input().split())
        dp = [0]*(n+1)
        dp[-1] = 1
        # brute force
        # for i in range(n, 1, -1):
        #     for j in range(1, i):
        #         dp[j] = (dp[j] + dp[i]) % mod
        #     for j in range(2, i+1):
        #         dp[i//j] = (dp[i] + dp[i//j]) % mod
        # print(dp[1])
        """
        2^(n-2) ways by addition alone? yes
        """
        # for i in range(n-1, 0, -1):
        #     by_addition = pow(2, n-i-1, mod)
        # print("power =", pow(2, n-2, mod))
        current = 1
        suffix_sum = [0]*(n+1)
        suffix_sum[-1] = 1
        for i in range(n-1, 0, -1):
            dp[i] = suffix_sum[i+1]
            # for j in range(2*i, n+1, i):
            #     dp[i] = (dp[i] + suffix_sum[j] -
            #              (suffix_sum[j+j] if j+j < n else 0))  # % mod
            #     break
            for j in range(2, n+1):
                if i*j > n:
                    break
                dp[i] += suffix_sum[i*j] - (suffix_sum[i*j+j] if i*j+j <= n else 0)
                dp[i] %= mod
            suffix_sum[i] = (suffix_sum[i+1] + dp[i]) % mod
        # print(dp)
        # print(suffix_sum)
        print(dp[1] % mod)
    
    
def main():
        t = 1
        # t = int(input())
        for _ in range(t):
            solve()
    
    
    if __name__ == "__main__":
        start_time = perf_counter()
        main()
        print(perf_counter()-start_time, file=sys.stderr)