    # ------------------- fast io --------------------
    import os
    import sys
    from io import BytesIO, IOBase
     
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
    # ------------------- fast io --------------------
    from collections import deque
    n=int(input())
    #rock,scizzors,paper
    alice=list(map(int,input().split()))
    bob=list(map(int,input().split()))
    maxnum=min(alice[0],bob[1])+min(alice[1],bob[2])+min(alice[2],bob[0])
    #3!*3! possibilities
    a=[("r",alice[0]),("s",alice[1]),("p",alice[2])]
    b=[("r",bob[0]),("s",bob[1]),("p",bob[2])]
    posa=[(a[0],a[1],a[2]),(a[0],a[2],a[1]),
         (a[1],a[2],a[0]),(a[1],a[0],a[2]),
         (a[2],a[1],a[0]),(a[2],a[0],a[1])]
    posb=[(b[0],b[1],b[2]),(b[0],b[2],b[1]),
         (b[1],b[0],b[2]),(b[1],b[2],b[0]),
         (b[2],b[0],b[1]),(b[2],b[1],b[0])]
    minans=10**9 +1
    k=0
    for s in range(6):
        perm1=posa[s]
        for i in range(6):
            perm2=posb[i]
            ans=0;leftover=deque([]);prev=deque([]);cv=deque([])
            for j in range(3):
                a1=perm1[j];b1=perm2[j]
                c1=a1[1];c2=b1[1]
                if len(leftover)>0:
                    while len(leftover)>0:
                        if cv[0]==0:
                            v1=min(leftover[0],c2)
                            if prev[0]=="r" and b1[0]=="s":
                                ans+=v1
                            elif prev[0]=="s" and b1[0]=="p":
                                ans+=v1
                            elif prev[0]=="p" and b1[0]=="r":
                                ans+=v1
                            c2-=v1;leftover[0]-=v1
                        else:
                            v1=min(leftover[0],c1)
                            if prev[0]=="r" and a1[0]=="p":
                                ans+=v1
                            elif prev[0]=="s" and a1[0]=="r":
                                ans+=v1
                            elif prev[0]=="p" and a1[0]=="s":
                                ans+=v1
                            c1-=v1;leftover[0]-=v1
                        if leftover[0]==0:
                            leftover.popleft();cv.popleft();prev.popleft()
                        elif v1==0:
                            break
                v0=min(c1,c2);c1-=v0;c2-=v0
                if a1[0]=="r" and b1[0]=="s":
                    ans+=v0
                elif a1[0]=="s" and b1[0]=="p":
                    ans+=v0
                elif a1[0]=="p" and b1[0]=="r":
                    ans+=v0
                if c1>0:
                    leftover.append(c1);cv.append(0);prev.append(a1[0])
                elif c2>0:
                    leftover.append(c2);cv.append(1);prev.append(b1[0])
            minans=min(minans,ans)
    print(minans,maxnum)