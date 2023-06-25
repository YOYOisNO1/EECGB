    #from bisect import bisect_left as bl                #c++ lowerbound bl(array,element)
    #from bisect import bisect_right as br               #c++ upperbound br(array,element)
    #from __future__ import print_function, division    #while using python2
    # from itertools import accumulate
    # from collections import defaultdict, Counter
    from collections import deque
    
def get_max(A, B):
        a1, a2, a3 = list(A)
        b1, b2, b3 = list(B)
        return min(a1,b2)+min(a2,b3)+min(a3,b1)
    
def get_min(A, B):
        a1, a2, a3 = list(A)
        b1, b2, b3 = list(B)
        k = min(a1, b3+b1)
        a1 -= k
        b3 -= k
        if b3 < 0:
            b1 += b3
            b3 = 0
        
        k = min(a2, b1+b2)
        a2 -= k
        b1 -= k
        if b1 < 0:
            b2 += b1
            b1 = 0
    
        k = min(a3, b2+b3)
        a3 -= k
        b2 -= k
        if b2 < 0:
            b3 += b2
            b2 = 0
        
        return get_max([a1, a2, a3], [b1, b2, b3])
    
def main():
        #sys.stdin = open('input.txt', 'r')
        #sys.stdout = open('output.txt', 'w')
    
        n = int(input())
        A = deque([int(x) for x in input().split()])
        B = deque([int(x) for x in input().split()])
    
        mx = 0
        mn = int(1e9) + 9
    
        mx = max(mx, get_max(A, B))
        mn = min(mn, get_min(A, B))
        A.rotate(1)
        B.rotate(1)
        mx = max(mx, get_max(A, B))
        mn = min(mn, get_min(A, B))
        A.rotate(1)
        B.rotate(1)
        mx = max(mx, get_max(A, B))
        mn = min(mn, get_min(A, B))
        print(mn, mx)
        
    #------------------ Python 2 and 3 footer by Pajenegod and c1729-----------------------------------------
    py2 = round(0.5)
    if py2:
        from future_builtins import ascii, filter, hex, map, oct, zip
        range = xrange
    
    import os, sys
    from io import IOBase, BytesIO
    
    BUFSIZE = 8192
    class FastIO(BytesIO):
        newlines = 0
    def __init__(self, file):
            self._file = file
            self._fd = file.fileno()
            self.writable = "x" in file.mode or "w" in file.mode
            self.write = super(FastIO, self).write if self.writable else None
    
    def _fill(self):
            s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.seek((self.tell(), self.seek(0,2), super(FastIO, self).write(s))[0])
            return s
    def read(self):
            while self._fill(): pass
            return super(FastIO,self).read()
    
    def readline(self):
            while self.newlines == 0:
                s = self._fill(); self.newlines = s.count(b"\n") + (not s)
            self.newlines -= 1
            return super(FastIO, self).readline()
    
    def flush(self):
            if self.writable:
                os.write(self._fd, self.getvalue())
                self.truncate(0), self.seek(0)
    
    class IOWrapper(IOBase):
    def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            if py2:
                self.write = self.buffer.write
                self.read = self.buffer.read
                self.readline = self.buffer.readline
            else:
                self.write = lambda s:self.buffer.write(s.encode('ascii'))
                self.read = lambda:self.buffer.read().decode('ascii')
                self.readline = lambda:self.buffer.readline().decode('ascii')
    
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip('\r\n')
    
    if __name__ == '__main__':
       main()