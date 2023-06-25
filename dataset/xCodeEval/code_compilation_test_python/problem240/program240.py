    
    
def main():
        n, k = inputi()
        @lru_cache(None)
    def F(f):
            if f > n:
                return 0
            if f % 2:
                return 1 + F(f * 2)
            return 1 + F(f * 2) + F(f + 1)
        odd = find_ge(range(1, n + 1, 2)[::-1], k, F, -inf)
        even = find_ge(range(2, n + 1, 2)[::-1], k, F, -inf)
        print(max(odd, even))
    
    
    # region bisect
    # 二分搜索，标准库没有函数参数
    
    import builtins
    
def len(a):
        if isinstance(a, range):
            return -((a.start - a.stop) // a.step)
        return builtins.len(a)
    
def bisect_left(a, x, key = None, lo = 0, hi = None):
        if lo < 0: lo = 0
        if hi == None: hi = len(a)
        if key == None: key = do_nothing
        while lo < hi:
            mid = (lo + hi) // 2
            if key(a[mid]) < x: lo = mid + 1
            else: hi = mid
        return lo
def bisect_right(a, x, key = None, lo = 0, hi = None):
        if lo < 0: lo = 0
        if hi == None: hi = len(a)
        if key == None: key = do_nothing
        while lo < hi:
            mid = (lo + hi) // 2
            if x < key(a[mid]): hi = mid
            else: lo = mid + 1
        return lo
def insort_left(a, x, key = None, lo = 0, hi = None):
        lo = bisect_left(a, x, key, lo, hi)
        a.insert(lo, x)
def insort_right(a, x, key = None, lo = 0, hi = None):
        lo = bisect_right(a, x, key, lo, hi)
        a.insert(lo, x)
    do_nothing = lambda x: x
    bisect = bisect_right
    insort = insort_right
def index(a, x, key = None, default = None, lo = 0, hi = None):
        if lo < 0: lo = 0
        if hi == None: hi = len(a)
        if key == None: key = do_nothing
        i = bisect_left(a, x, key, lo, hi)
        if lo <= i < hi and key(a[i]) == x: return a[i]
        if default != None: return default
        raise ValueError
def find_lt(a, x, key = None, default = None, lo = 0, hi = None):
        if lo < 0: lo = 0
        if hi == None: hi = len(a)
        i = bisect_left(a, x, key, lo, hi)
        if lo < i <= hi: return a[i - 1]
        if default != None: return default
        raise ValueError
def find_le(a, x, key = None, default = None, lo = 0, hi = None):
        if lo < 0: lo = 0
        if hi == None: hi = len(a)
        i = bisect_right(a, x, key, lo, hi)
        if lo < i <= hi: return a[i - 1]
        if default != None: return default
        raise ValueError
def find_gt(a, x, key = None, default = None, lo = 0, hi = None):
        if lo < 0: lo = 0
        if hi == None: hi = len(a)
        i = bisect_right(a, x, key, lo, hi)
        if lo <= i < hi: return a[i]
        if default != None: return default
        raise ValueError
def find_ge(a, x, key = None, default = None, lo = 0, hi = None):
        if lo < 0: lo = 0
        if hi == None: hi = len(a)
        i = bisect_left(a, x, key, lo, hi)
        if lo <= i < hi: return a[i]
        if default != None: return default
        raise ValueError
    
    # endregion
    
    
    # region M
    
    # region fastio
    
    import sys, io, os
    sys.setrecursionlimit(10000)
    BUFSIZE = 8192
    class FastIO(io.IOBase):
        newlines = 0
    def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = io.BytesIO()
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
    class IOWrapper(io.IOBase):
    def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
     
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().strip()
    
    # endregion
    
    # region import
    
    inputt = lambda t = 0: range(t) if t else range(int(input()))
    inputi = lambda: map(int, input().split())
    inputl = lambda: list(inputi())
    from math import *
    from heapq import *
    from itertools import *
    from functools import reduce, lru_cache
    from collections import Counter, defaultdict
    import re, copy, operator, cmath
    
    # endregion
    
    # region main
    
    if __name__ == "__main__":
        main()
    
    # endregion
    
    # endregion