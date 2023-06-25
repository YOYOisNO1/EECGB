    # Fast IO Region
    import os,sys
    from io import BytesIO, IOBase
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
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    in1 = lambda : int(input())
    in2 = lambda : list(map(int, input().split()))
    #Solve
    import math
    mod = 998244353
    
    class obj(int):
    def __add__(self, __x: int) -> int:
            return super().__add__(__x) % mod
    def __mul__(self, __x: int) -> int:
            return super().__mul__(__x) % mod
    def __radd__(self, __x: int) -> int:
            return super().__radd__(__x) % mod
    def __rmul__(self, __x: int) -> int:
            return super().__rmul__(__x) % mod
    
def main():
        n, x = list(map(obj, input().split()))
        c = [[obj(0) for _ in range(505)] for _ in range(505)]
        dp = [[obj(0) for _ in range(505)] for _ in range(505)]
    
        for i in range(n + 1):
            c[i][0] = c[i][i] = obj(1)
            for j in range(1, i):
                c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
        dp[n][0] = obj(1)
        for i in reversed(range(2, n + 1)):
            for j in range(x):
                if dp[i][j] == obj(0):
                    continue
                pw, nj = obj(1), obj(min(x, j + i - 1))
                for k in reversed(range(i + 1)):
                    dp[k][nj] = dp[k][nj] + dp[i][j] * c[i][k] * pw
                    pw = pw * (nj - obj(j))
        res = obj(0)
        for i in range(x + 1):
            res += dp[0][i]
        print(res % mod)
    
    if __name__ == "__main__":
        main()