    #! /usr/bin/python3
    
    import os
    import sys
    from io import BytesIO, IOBase
    import math
    
    
def main1():
        for _ in range(int(input())):
            n, x = map(int, input().split())
            if n <= 2:
                print(1)
            else:
                n -= 2
                print(1 + math.ceil(n / x))
            
def main2():
        for _ in range(int(input())):
            n, m = map(int, input().split())
            flag  = 0
            for i in range(n):
                mat = []
                for j in range(2):
                    mat.append(list(map(int, input().split())))
                if mat[0][1] == mat[1][0]:
                    flag = 1
            if m % 2 or flag == 0:
                print("NO")
            else:
                print("YES")
    
def main3():
        for _ in range(int(input())):
            n = int(input())
            ans = float("inf")
            for i in range(1, math.floor(math.sqrt(n)) + 1):
                ans = min(ans, i - 1 + ((n  -i) + i - 1) // i)
            print(ans)
    
def main4():
        n = int(input())
        a = list(map(int, input().split()))
        ls = [0] * n
        ls[0] = a[0]
        for i in range(1, n):
            ls[i] = ls[i-1] + a[i]
        ans = 0
        d = dict()
        d[0] = 0
        d[ls[0]] = 0
        prev_pos = 0
        for i in range(1, n):
            if ls[i] in d:
                pos = d[ls[i]] + 1
                if pos >= prev_pos:
                    prev_pos = i
                    ans += 1
            d[ls[i]] = i
        print(ans)
    
    
def main5():
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    
        max_win = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
        min_win = max(0, a[0] - b[0] - b[2]) + max(0, a[1] - b[1] - b[0]) + max(0, a[2] - b[2] - b[1])
        print(min_win, max_win)
    
    
def main6():
        pass
    
    
    
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
        main5()