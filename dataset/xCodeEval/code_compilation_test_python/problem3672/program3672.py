    import os
    import sys
    from io import BytesIO, IOBase
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
    input = lambda: sys.stdin.readline()
     
    # ------------------------------
     
def RL(): return map(int, sys.stdin.readline().split())
def RLL(): return list(map(int, sys.stdin.readline().split()))
def N(): return int(input())
def print_list(l):
        print(' '.join(map(str,l)))
    # import heapq as hq
    # import bisect as bs
    # from collections import deque as dq
    # from collections import defaultdict as dc 
    # from math import ceil,floor,sqrt
    # from collections import Counter
    
    
    n,m = RL()
    dic = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,t = RL()
        dic[u].append((v,t))
        dic[v].append((u,t))
    v = [None] * (n+1)
    f = [True] * (n+1)
    key = {}
    color = [0]*(n+1)
    flag = True
    for s in range(1,n+1):
        if v[s] is not None: continue
        v[s] = 0
        color[s] = s
        now = [s]
        ss = [0]
        while now and flag:
            p = now.pop()
            for child,t in dic[p]:
                if v[child] is not None:
                    if f[child]!=f[p]:
                        if v[child]+v[p]!=t:
                            flag = False
                            break
                    elif f[child] is True:
                        if s not in key:
                            key[s] =  (v[child]+v[p]-t)/(-2)
                        elif v[child]+v[p]+key[s]*2!=t:
                            flag = False
                            break
                    else:
                        if s not in key:
                            key[s] =  (v[child]+v[p]-t)/2
                        elif v[child]+v[p]-key[s]*2!=t:
                            flag = False
                            break
                else:
                    v[child] = t-v[p]
                    ss.append(abs(v[child]))
                    f[child] = not f[p]
                    color[child] = s
                    now.append(child)
        if not flag:
            break
        if s not in key:
            ss.sort()
            nn = len(ss)
            key[s] = (ss[nn>>1]+ss[nn-1>>1])/2
    if flag:
        print("YES")
        res = []
        for i in range(1,n+1):
            if f[i]:
                res.append(v[i]+key[color[i]])
            else:
                res.append(v[i]-key[color[i]])
        print_list(res)
    else:
        print("NO")