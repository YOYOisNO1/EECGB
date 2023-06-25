    # by the authority of GOD     author: manhar singh sachdev #
    
    import os,sys
    from io import BytesIO, IOBase
    
def gen(x,m):
        bt = []
        for i in range(len(x)):
            for xx in range(len(bt)):
                bt.append((bt[xx]+x[i])%m)
            bt.append(x[i]%m)
        return sorted(set(bt))
    
def main():
        n,m = map(int,input().split())
        arr = list(map(int,input().split()))
        if n == 1:
            print(arr[0]%m)
            exit()
        a = gen(arr[n//2:],m)
        b = gen(arr[:n//2],m)
        ans = max((a[-1]+b[-1])%m,a[-1]%m,b[-1]%m)
        j = len(b)-1
        for i in range(len(a)):
            ans = max(ans,(a[i]+b[j])%m)
            while j != -1 and a[i]+b[j] >= m:
                j -= 1
                ans = max(ans,(a[i]+b[j])%m)
            if j == -1:
                break
        print(ans)
    
    #Fast IO Region
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
    
    if __name__ == '__main__':
        main()