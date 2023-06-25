    # by the authority of GOD     author: manhar singh sachdev #
    
    import os,sys
    from io import BytesIO, IOBase
    from itertools import permutations
    
def main():
        n = int(input())
        r1,s1,p1 = map(int,input().split())
        r2,s2,p2 = map(int,input().split())
        maxi = min(r1,s2)+min(s1,p2)+min(p1,r2)
        r3,s3,p3 = r2,s2,p2
        r4,s4,p4 = r1,s1,p1
        mini = 10**10
        for i in permutations([1,2,3]):
            dct = {1:r1,2:s1,3:p1}
            dct1 = {1:[r2,p2],2:[s2,r2],3:[p2,s2]}
            dct2 = {1: [p2, r2], 2: [r2, s2], 3: [s2, p2]}
            dct3 = {1:s2,2:p2,3:r2}
            ans = 0
            for x in i:
                r = min(dct[x],dct1[x][0])
                dct[x] -= r
                dct1[x][0] -= r
                q = min(dct[x],dct1[x][1])
                dct[x] -= q
                dct1[x][1] -= q
                dct3[x] -= dct[x]
                ans += dct[x]
                dct[x] = 0
            mini = min(mini,ans)
            r2,s2,p2 = r3,s3,p3
            r1,s1,p1 = r4,s4,p4
        print(mini,maxi)
    
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
    
    if __name__ == "__main__":
        main()