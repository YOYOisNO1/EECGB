    from __future__ import division, print_function
    import os
    import sys
    from __builtin__ import xrange as range
    from cStringIO import StringIO as BytesIO
    from future_builtins import ascii, filter, hex, map, oct, zip
    from io import IOBase
    
    
    from collections import defaultdict as ddic, Counter, deque
    from itertools import permutations
    from bisect import bisect
    
    
def solve(N, M, need, offers):
        # N microtransaction types
        # need need[i] of the ith type
    
        offers.sort()
        O = ddic(list)
        O2 = ddic(list)
        for d,t in offers:
            O[d].append(t-1)
            O2[t-1].append(d)
        NS = sum(need)
        
    def possible(day):
            cash = 0
            A = need[:]
            todo = NS
            for cur_day in xrange(1, day+1):
                cash += 1
                for t in O[cur_day]:
                    # if this is last chance
                    B = O2[t]
                    j = bisect(B, day)
                    if not any(0<= j2 < len(B) and cur_day < B[j2] <= day
                           for j2 in (j,j-1,j-2)):
                        delta = min(A[t], cash)
                        cash -= delta
                        A[t] -= delta
                        todo -= delta
                        if cash < 0: return False
            return cash >= 2 * todo
    
    
        lo, hi = 0, 2 * sum(need)
        while lo < hi:  #invariant: hi is possible
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo
        
        
def main():
        N, M = readlist()
        K = readlist()
        offers = [readlist() for _ in xrange(M)]
        print(solve(N,M,K,offers))
    
    # region template
    
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
    def __init__(self, file):
            self._buffer = BytesIO()
            self._fd = file.fileno()
            self._writable = "x" in file.mode or "r" not in file.mode
            self.write = self._buffer.write if self._writable else None
    
    def read(self):
            if self._buffer.tell():
                return self._buffer.read()
            return os.read(self._fd, os.fstat(self._fd).st_size)
    
    def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count("\n") + (not b)
                ptr = self._buffer.tell()
                self._buffer.seek(0, 2), self._buffer.write(b), self._buffer.seek(ptr)
            self.newlines -= 1
            return self._buffer.readline()
    
    def flush(self):
            if self._writable:
                os.write(self._fd, self._buffer.getvalue())
                self._buffer.truncate(0), self._buffer.seek(0)
    
    
    class ostream:
    def __lshift__(self, a):
            if a is endl:
                sys.stdout.write("\n")
                sys.stdout.flush()
            else:
                sys.stdout.write(str(a))
            return self
    
    
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
    
    
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
    cout, endl = ostream(), object()
    
    readline = sys.stdin.readline
    readlist = lambda var=int: [var(n) for n in readline().split()]
    input = lambda: readline().rstrip("\r\n")
    
    # endregion
    
    if __name__ == "__main__":
        main()