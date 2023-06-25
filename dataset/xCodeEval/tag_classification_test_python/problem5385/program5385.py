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
    #######################################
    a=1
    f=[1]*200001
    fi=[1]*200001
    m=10**9+7
    b=1
    for i in range(2,200001):
        a*=i
        a%=m
        f[i]=a
        b*=pow(i,m-2,m)
        b%=m
        fi[i]=b
    for  t in range(int(input())):
        n,k=map(int,input().split())
        if not k:
            print(1)
            continue
        dp=[[0]*2 for i in range(k)]
        a=0
        b=0
        for i in range(1,n):
            if i%2:
                a+=f[n]*fi[n-i]*fi[i]
                a%=m
            else:
                b+=f[n]*fi[n-i]*fi[i]
                b%=m
        a+=1
        b+=1
        a%=m
        b%=m
        if n%2:
            dp[0][0]=a
        else:
            dp[0][0]=b
        dp[0][1]=1
        x=pow(2,n,m)
        y=x
        for i in range(1,k):
            if n%2:
                dp[i][0]=a*(dp[i-1][0]+dp[i-1][1])
            else:
                dp[i][0]=b*(dp[i-1][0]+dp[i-1][1])
            if n%2:
                dp[i][1]=dp[i-1][0]+dp[i-1][1]
            else:
                dp[i][1]=y
                y*=x
                y%=m
            dp[i][0]%=m       
            dp[i][1]%=m
        print((dp[k-1][0]+dp[k-1][1])%m)
        
                