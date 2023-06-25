    #!/usr/bin/env python
    
    #IMPORTS
    
    
def solve():
        global mod
    
        mod = 10**9+7
    
        global powlist
    
        powlist = [1]
    
        for i in range(1, 200000+1):
    
            powlist.append((powlist[-1]*2)%mod)
    
        N, k = map(int, input().split())
    
        finaladdlist = [1]
    
        for i in range(k):
    
            finaladdlist.append((finaladdlist[-1]*powlist[N])%mod)
    
        if N % 2:
    
            solutionofans = pow(2, N*k, mod)
    
            for i in range(k): solutionofans -= ((((pow(powlist[N-1]+1, i, mod)) * (powlist[N-1]-1))%mod) * finaladdlist[k-i-1])%mod
            
            return solutionofans % mod
        else:
    
            solutionofans = pow(2, N*k, mod)
    
            for i in range(k): solutionofans -= ((((pow(powlist[N-1]-1, i, mod)) * (powlist[N-1]))%mod) * finaladdlist[k-i-1])%mod
            
            return solutionofans % mod
    
    
def main():
        for testcases in range(int(input())):
            print(solve())
    
    
        #print(solve())
    
    #****************************************************************************************
def input():#****************************************************************************
        return sys.stdin.readline().rstrip()
    from io import BytesIO, IOBase#**********************************************************
    import os, sys#**************************************************************************
    BUFSIZE = 8192#**************************************************************************
    class FastIO(IOBase):#*******************************************************************
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
    class IOWrapper(IOBase):#****************************************************************
    def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)#*********************
    if __name__ == "__main__":#**************************************************************
        main()
    #****************************************************************************************