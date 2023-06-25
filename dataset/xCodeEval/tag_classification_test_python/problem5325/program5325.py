    #!/usr/bin/env python
    from __future__ import division, print_function
    
    import os
    import sys
    from io import BytesIO, IOBase
    
    if sys.version_info[0] < 3:
        from __builtin__ import xrange as range
        from future_builtins import ascii, filter, hex, map, oct, zip
    
    
    class LazySegmentTree:
    def __init__(self, data, default=0, func=max, mod=-1):
            """initialize the lazy segment tree with data"""
            self.m = mod
    
            self._default = default
            self._func = func
    
            self._len = len(data)
            self._size = _size = 1 << (self._len - 1).bit_length()
            self._lazy = [0] * (2 * _size)
    
            self.data = [default] * (2 * _size)
            self.data[_size:_size + self._len] = data
            for i in reversed(range(_size)):
                self.data[i] = func(self.data[i + i], self.data[i + i + 1])
    
    def __len__(self):
            return self._len
    
    def _push(self, idx):
            """push query on idx to its children"""
            # Let the children know of the queries
            q, self._lazy[idx] = self._lazy[idx], 0
    
            self._lazy[2 * idx] = (self._lazy[2 * idx] + q) % self.m
            self._lazy[2 * idx + 1] = (self._lazy[2 * idx + 1] + q) % self.m
            self.data[2 * idx] = (self.data[2 * idx] + q) % self.m
            self.data[2 * idx + 1] = (self.data[2 * idx + 1] + q) % self.m
    
    def _update(self, idx):
            """updates the node idx to know of all queries applied to it via its ancestors"""
            for i in reversed(range(1, idx.bit_length())):
                self._push(idx >> i)
    
    def _build(self, idx):
            """make the changes to idx be known to its ancestors"""
            idx >>= 1
            while idx:
                self.data[idx] = (self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]) % self.m
                idx >>= 1
    
    def add(self, start, stop, value):
            """lazily add value to [start, stop)"""
            start = start_copy = start + self._size
            stop = stop_copy = stop + self._size
            while start < stop:
                if start & 1:
                    self._lazy[start] = (self._lazy[start] + value) % self.m
                    self.data[start] = (self.data[start] + value) % self.m
                    start += 1
                if stop & 1:
                    stop -= 1
                    self._lazy[stop] = (self._lazy[stop] + value) % self.m
                    self.data[stop] = (self.data[stop] + value) % self.m
                start >>= 1
                stop >>= 1
    
            # Tell all nodes above of the updated area of the updates
            self._build(start_copy)
            self._build(stop_copy - 1)
    
    def query(self, start, stop, default=0):
            """func of data[start, stop)"""
            start += self._size
            stop += self._size
    
            # Apply all the lazily stored queries
            self._update(start)
            self._update(stop - 1)
    
            res = default
            while start < stop:
                if start & 1:
                    res = self._func(res, self.data[start])
                    start += 1
                if stop & 1:
                    stop -= 1
                    res = self._func(res, self.data[stop])
                start >>= 1
                stop >>= 1
            return res
    
    def __getitem__(self, idx):
            return self.query(idx, idx + 1)
    
    def __repr__(self):
            return "LazySegmentTree({0})".format(self.data)
    
    
def main():
        n, m = map(int, input().split())
    
        sol = LazySegmentTree([0] * (n + 1), mod=m)
        sol.add(1, 2, 1)
    
        for i in range(1, n):
            sol.add(i + 1, n + 1, sol[i])
            for j in range(2, (n // i) + 1):
                sol.add(i * j, min(n + 1, (i + 1) * j), sol[i])
    
        print(sol[n])
    
    
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