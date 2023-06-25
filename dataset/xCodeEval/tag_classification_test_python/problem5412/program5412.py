    from collections import defaultdict, Counter,deque
    from math import sqrt, log10, log, floor, factorial,gcd
    from bisect import bisect_left, bisect_right
    from itertools import permutations,combinations
    import sys, io, os
    input = sys.stdin.readline
    # input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    # sys.setrecursionlimit(10000)
    inf = float('inf')
    mod = 10 ** 9 + 7
def get_list(): return [int(i) for i in input().split()]
def yn(a): print("YES" if a else "NO")
    ceil = lambda a, b: (a + b - 1) // b
    import os
    import sys
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
    
    
    t=int(input())
    for i in range(t):
        n,k=[int(i) for i in input().split()]
        if n%2==0:
            p = pow(2, n - 1,mod)
            pp = pow(2, n,mod)
            ans=0
            for i in range(k):
                # u = (pow(p, k - i - 1,mod) * pow(pp, i,mod)) % mod
                u = (pow((p - 1 + mod) % mod, k - i - 1,mod) * pow(pp, i,mod)) % mod
                ans = (ans + u) % mod
    
            ans = (ans + pow((p - 1 + mod) % mod, k,mod))
            ans %= mod
            print(ans)
        else:
    
            p = pow(2, n - 1, mod)
            pp = pow(2, n, mod)
            ans = 0
            for i in range(k):
                # u = (pow(p, k - i - 1,mod) * pow(pp, i,mod)) % mod
                u = (pow(p, k - i - 1,mod) * pow((p + 1) % mod, i,mod)) % mod;
                ans = (ans + u) % mod
    
            ans = (ans + pow(p , k,mod))
            ans %= mod
            print(ans)