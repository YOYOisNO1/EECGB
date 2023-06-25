    from collections import *
    import os, sys
    from io import BytesIO, IOBase
    
    
    class FastIO(IOBase):
        newlines = 0
    
    def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
    
    def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
    
    def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
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
    r = lambda dtype: dtype(input().strip())
    rd = lambda dtype: [dtype(x) for x in input().split()]
    r2d = lambda dtype, n: [r(dtype) for _ in range(n)]
    rs2d = lambda dtype, n: [rd(dtype) for _ in range(n)]
    r_enu = lambda dtype: [(i, x) for i, x in enumerate(rd(dtype))]
    rs_enu = lambda dtype, n: [[i, rd(dtype)] for i in range(n)]
    
    ceil1, mod = lambda a, b: (a + b - 1) // b, 10 ** 9 + 7
    add = lambda a, b: (a + b) % mod
    mult = lambda a, b: (a * b) % mod
    
    for _ in range(r(int)):
        n, k = rd(int)
        cur, ans, parity = 1, 0, (n & 1 == 0)
    
        for i in range(k - 1, -1, -1):
            ans = add(ans, mult(cur * parity, pow(pow(2, i, mod), n, mod)))
            cur = mult(cur, add(pow(2, n - 1, mod), -parity if parity else 1))
    
        print(add(ans, cur))