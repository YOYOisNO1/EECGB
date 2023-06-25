    #!/usr/bin/env python
    from __future__ import division, print_function
    
    import os
    import sys
    from collections import Counter
    from io import BytesIO, IOBase
    from math import gcd
    
    if sys.version_info[0] < 3:
        from __builtin__ import xrange as range
        from future_builtins import ascii, filter, hex, map, oct, zip
    
    
def memodict(f):
        """memoization decorator for a function taking a single argument"""
        class memodict(dict):
        def __missing__(self, key):
                ret = self[key] = f(key)
                return ret
    
        return memodict().__getitem__
    
    
def pollard_rho(n):
        """returns a random factor of n"""
        if n & 1 == 0:
            return 2
        if n % 3 == 0:
            return 3
    
        s = ((n - 1) & (1 - n)).bit_length() - 1
        d = n >> s
        for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
            p = pow(a, d, n)
            if p == 1 or p == n - 1 or a % n == 0:
                continue
            for _ in range(s):
                prev = p
                p = (p * p) % n
                if p == 1:
                    return gcd(prev - 1, n)
                if p == n - 1:
                    break
            else:
                for i in range(2, n):
                    x, y = i, (i * i + 1) % n
                    f = gcd(abs(x - y), n)
                    while f == 1:
                        x, y = (x * x + 1) % n, (y * y + 1) % n
                        y = (y * y + 1) % n
                        f = gcd(abs(x - y), n)
                    if f != n:
                        return f
        return n
    
    
    @memodict
def prime_factors(n):
        """returns a Counter of the prime factorization of n"""
        if n <= 1:
            return Counter()
        f = pollard_rho(n)
        return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)
    
    
def main():
        n = int(input())
    
        f = list(prime_factors(n).keys())
        if len(f) == 1:
            print(f[0])
        else:
            print(1)
    
    
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
    
    
def print(*args, **kwargs):
        """Prints the values to a stream, or to sys.stdout by default."""
        sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
        at_start = True
        for x in args:
            if not at_start:
                file.write(sep)
            file.write(str(x))
            at_start = False
        file.write(kwargs.pop("end", "\n"))
        if kwargs.pop("flush", False):
            file.flush()
    
    
    if sys.version_info[0] < 3:
        sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
    else:
        sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    
    # endregion
    
    if __name__ == "__main__":
        main()