    from __future__ import print_function
    from math import log
    from collections import defaultdict, deque
    import os
    import random
    import sys
    from io import BytesIO, IOBase
    #import time
     
def main():
        pass
     
    # region fastio
     
    BUFSIZE = 8192
def lcm(a,b):
        return (a*b)//gcd(a,b)
def ceilDiv(a,b):
        if a%b==0:
            return a//b
        else:
            return a//b+1
     
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
    class myDict:
    def __init__(self,func):
            self.RANDOM = random.randint(0,1<<32)
            self.default=func
            self.dict={}
    def __getitem__(self,key):
            myKey=self.RANDOM^key
            if myKey not in self.dict:
                self.dict[myKey]=self.default()
            return self.dict[myKey]
    def __setitem__(self,key,item):
            myKey=self.RANDOM^key
            self.dict[myKey]=item
    def getKeys(self):
            return [self.RANDOM^i for i in self.dict]
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    #sys.stdin, sys.stdout =open("test.txt","r"),open("result.txt","w")
    #ini=time.time()
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    mod=998244353 
    ############ ---- Input Functions ---- ############
def inp():
        return(int(input()))
def inlt():
        return(list(map(int,input().split())))
def insr():
        s = input()
        return(list(s[:len(s) ]))
def invr():
        return(map(int,input().split()))
def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
        max_n = min(max_n, mod - 1)
    
        fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
        fact[0] = 1
        for i in range(max_n):
            fact[i + 1] = fact[i] * (i + 1) % mod
    
        inv_fact[-1] = pow(fact[-1], mod - 2, mod)
        for i in reversed(range(max_n)):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    def nCr_mod(n, r):
            res = 1
            while n or r:
                a, b = n % mod, r % mod
                if a < b:
                    return 0
                res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
                n //= mod
                r //= mod
            return res
    
        return nCr_mod
    
    nCr=make_nCr_mod(500,mod)
    n,k=invr()
    dp=[[0]*(k+1) for i in range(n+1)]
    
    for i in range(k+1):
        dp[1][i]=1
        #dp[2][i]=i
    for i in range(2,n+1):
        for j in range(1,k+1):
            for t in range(1,i+1):
                left=i-t
                
                dp[i][j]+=nCr(i-1,left)*dp[t][j-1]*pow(k-j+1,left*(t-1)+(left*(left-1))//2,mod)
                dp[i][j]%=mod
                
    print(dp[n][k])