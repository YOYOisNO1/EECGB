    #!/usr/bin/env pypy
    from __future__ import division, print_function
    
    import os
    import sys
    from __builtin__ import xrange as range
    from cStringIO import StringIO
    from future_builtins import ascii, filter, hex, map, oct, zip
    from io import IOBase
    
    import __pypy__
    
    
def iroot(n, k=2):
        if n == 0:
            return 0
        if n < 0:
            return -iroot(-n, k) if k & 1 else None
        u, s = n, n + 1
        while u < s:
            s = u
            t = (k - 1) * s + n // s**(k - 1)
            u = t // k
        return s
    
    
def main():
        k = int(input())
        cf = [list(x) for x in list('codeforces')]
        cnt = 1
        while cnt < k:
            d = min(len(x) for x in cf)
            for i in range(10):
                if len(cf[i]) == d:
                    cf[i].append(cf[i][-1])
                    break
            cnt = 1
            for i in range(10):
                cnt *= len(cf[i])
    
        print(''.join(''.join(x) for x in cf))
    
    
    # region fastio
    
    BUFSIZE = 8192
    
    
    class FastI(IOBase):
    def __init__(self, file):
            self._fd = file.fileno()
            self._buffer = StringIO()
            self.newlines = 0
    
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
                self.newlines = b.count("\n") + (not b)
                ptr = self._buffer.tell()
                self._buffer.seek(0,
                                  2), self._buffer.write(b), self._buffer.seek(ptr)
            self.newlines -= 1
            return self._buffer.readline()
    
    
    class FastO(IOBase):
    def __init__(self, file):
            self._fd = file.fileno()
            self._buffer = __pypy__.builders.StringBuilder()
            self.write = lambda s: self._buffer.append(s)
    
    def flush(self):
            os.write(self._fd, self._buffer.build())
            self._buffer = __pypy__.builders.StringBuilder()
    
    
def print(*args, **kwargs):
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
    
    
    sys.stdin, sys.stdout = FastI(sys.stdin), FastO(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    
    # endregion
    
    if __name__ == "__main__":
        main()