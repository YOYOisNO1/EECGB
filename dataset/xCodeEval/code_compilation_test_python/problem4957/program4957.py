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
    
    
    n = N()
    dic = [set() for _ in range(n+1)]
    dic2 = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = RL()
        dic[u].add(v)
        dic[v].add(u)
    now = [1]
    father,gress,leaf = [0]*(n+1),[0]*(n+1),[]
    for i in range(2,n+1):
        gress[i] = len(dic[i])-1
        if gress[i]==0:
            leaf.append(i)
    while now:
        node = now.pop()
        dic[node].discard(father[node])
        for child in dic[node]:
            father[child] = node 
            now.append(child)
    res = 0
    ans = [0]*(n+1)
    while leaf:
        p = leaf.pop()
        f = father[p]
        if not dic2[p]:
            dic2[f].append(p)
        else:
            t = len(dic2[p])
            res+=t*2
            while t>2:
                t-=2
                a,b = dic2[p].pop(),dic2[p].pop()
                ans[a] = b 
                ans[b] = a 
            if t==1:
                a = dic2[p].pop()
                ans[a] = p 
                ans[p] = a 
            else:
                a,b = dic2[p].pop(),dic2[p].pop()
                ans[a] = p 
                ans[p] = b 
                ans[b] = a 
        gress[f]-=1
        if gress[f]==0:
            leaf.append(f)
    p = 1
    if not dic2[p]:
        res+=2
        m = dic[p].pop()
        b = ans[m]
        a = ans[b]
        if a!=m:
            ans[a] = b 
            ans[m] = p 
            ans[p] = m 
        else:
            ans[p] = m 
            ans[m] = b 
            ans[b] = p
    else:
        t = len(dic2[p])
        res+=t*2
        while t>2:
            t-=2
            a,b = dic2[p].pop(),dic2[p].pop()
            ans[a] = b 
            ans[b] = a 
        if t==1:
            a = dic2[p].pop()
            ans[a] = p 
            ans[p] = a 
        else:
            a,b = dic2[p].pop(),dic2[p].pop()
            ans[a] = p 
            ans[p] = b 
            ans[b] = a 
    print(res)
    print_list(ans[1:])