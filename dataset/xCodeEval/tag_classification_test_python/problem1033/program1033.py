    # Legends Always Come Up with Solution
    # Author: Manvir Singh
    
    import os
    from io import BytesIO, IOBase
    import sys
    from collections import defaultdict,deque,Counter
    from bisect import *
    from math import sqrt
    import math
    from itertools import permutations
    
def main():
        n=int(input())
        c=list(map(int,input().split()))
        d=list(map(int,input().split()))
        ma=min(c[0],d[1])+min(c[1],d[2])+min(c[2],d[0])
        m=0
        for i in permutations([0,1,2,3,4,5]):
            ans=0
            a=c[:]
            b=d[:]
            for j in i:
                if j<3:
                    x=min(a[j],b[j])
                    a[j]-=x
                    b[j]-=x
                    ans+=x
                else:
                    x=min(b[j-3],a[(j-2)%3])
                    b[j-3]-=x
                    a[(j-2)%3]-=x
                    ans+=x
            m=max(m,ans)
        mi=n-m
        print(mi,ma)
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
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    
    if __name__ == "__main__":
        main()