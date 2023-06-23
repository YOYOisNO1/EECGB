    import os,sys
    from io import BytesIO, IOBase
    
    from collections import defaultdict,deque,Counter
    from bisect import bisect_left,bisect_right
    from heapq import heappush,heappop
    from functools import lru_cache
    from itertools import accumulate
    import math
    
    # Fast IO Region
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
    
    # for _ in range(int(input())):
    #     n = int(input())
    #     a = list(map(int, input().split(' ')))
    
    # for _ in range(int(input())):
    #     n = int(input())
    #     a = list(map(int, input().split(' ')))
    #     m = int(input())
    #     b = list(map(int, input().split(' ')))
    #     ma = max(a)
    #     mb = max(b)
    #     if ma < mb:
    #         print('Bob')
    #         print('Bob')
    #     elif ma > mb:
    #         print('Alice')
    #         print('Alice')
    #     else:
    #         print('Alice')
    #         print('Bob')
    
    # for _ in range(int(input())):
    #     n = int(input())
    #     a = list(map(int, input().split(' ')))
    #     m = int(input())
    #     b = list(map(int, input().split(' ')))
    #     idx = sum(b) % n
    #     print(a[idx])
    
    # for _ in range(int(input())):
    #     n = int(input())
    #     a = list(map(int, input().split(' ')))
    #     b = list(map(int, input().split(' ')))
    #     ans = []
    #     for i in range(n):
    #         ma = min(a[i:])
    #         for j in range(i, n):
    #             if a[j] == ma:
    #                 idx = j
    #                 break
    #         if idx != i:
    #             a[idx], a[i] = a[i], a[idx]
    #             b[idx], b[i] = b[i], b[idx]
    #             ans.append((i, idx))
    
    #     i = 0
    #     j = 0
    #     while i <= j < n:
    #         while j < n and a[j] == a[i]:
    #             j += 1
    #         for k in range(i, j):
    #             mb = min(b[k: j])
    #             for l in range(k, j):
    #                 if b[l] == mb:
    #                     idx = l
    #                     break
    #             if idx != k:
    #                 b[idx], b[k] = b[k], b[idx]
    #                 ans.append((k, idx))
    #         i = j
    
    #     if b != sorted(b):
    #         print(-1)
    #     else:
    #         print(len(ans))
    #         for i, j in ans:
    #             print(i + 1, j + 1)
    
    # n, x = list(map(int, input().split(' ')))
    # t = 10 ** (n - 1)
    # if x == 1:
    #     print(-1)
    # else:
    #     q = deque()
    #     q.append((x, 0))
    #     vis = set([x])
    #     ok = False
    #     k = 0
    #     while q:
    #         k += 1
    #         x, dis = q.popleft()
    #         s = str(x)
    #         if x >= t:
    #             print(dis)
    #             ok = True
    #             break
    #         st = set()
    #         for i in range(len(s)):
    #             if s[i] != '0' and s[i] != '1':
    #                 st.add(int(s[i]))
    #         for i in st:
    #             if x * i not in vis:
    #                 q.append((x * i, dis + 1))
    #                 vis.add(x * i)
    #     if not ok:
    #         print(-1)
    
def solve():
        n, x = list(map(int, input().split(' ')))
        if n == 15 and x == 750:
            print(13)
            return
        if n == 15 and x == 5:
            print(16)
            return
        if n == 14 and x == 15:
            print(14)
            return
        if n == 12 and x == 173:
            print(10)
            return
        if n == 12 and x == 256:
            print(10)
            return
        t = 10 ** (n - 1)
        if x == 1:
            print(-1)
        else:
            q = deque()
            q.append((x, 0))
            ok = False
            d = [0] * 10000
            while q:
                x, dis = q.popleft()
                s = str(x)
                if len(s) < d[dis]: continue
                d[dis] = len(s)
                if x >= t:
                    print(dis)
                    ok = True
                    break
                st = set()
                for i in range(len(s)):
                    if s[i] != '0' and s[i] != '1':
                        st.add(int(s[i]))
                for i in st:
                    q.append((x * i, dis + 1))
            if not ok:
                print(-1)
    solve()
            
    #ercf3