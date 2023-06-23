    #!/usr/bin/env python
    import os
    import sys
    from io import BytesIO, IOBase
    from typing import Tuple
    
    arr, d = [None] * 2
    
    
def possible(x: float) -> bool:
        global arr, d
        
        l = [i - x for i in arr]
        for i in range(1, len(l)):
            l[i] += l[i-1]
        mn = [0]
        for i in range(1, len(l)):
            prev = mn[-1]
            if l[prev] < l[i]:
                mn.append(prev)
            else:
                mn.append(i)
    
    
        for r in range(d, len(l)):
            if l[r] - l[mn[r-d]] >= 0:
                return (r + 1, mn[r-d])[::-1]
        
        return (-1, -1)
    
    
    
def getInput() -> None:
        global arr, d
        n, d = map(int, input().split())
        arr = list(map(int, input().split()))
        print(possible(6.66666))
    
def main() -> None:
        getInput()
        
    
    
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
    
    # endregion
    
    if __name__ == "__main__":
        main()