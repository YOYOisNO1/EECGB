    #------------------------template--------------------------#
    import os
    import sys
    from math import *
    from collections import *
    from fractions import *
    from bisect import *
    from heapq import*
    from io import BytesIO, IOBase
def vsInput():
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
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
    ALPHA='abcdefghijklmnopqrstuvwxyz'
    MOD=1000000007
def value():return tuple(map(int,input().split()))
def array():return [int(i) for i in input().split()]
def Int():return int(input())
def Str():return input()
def arrayS():return [i for i in input().split()]
    
    #-------------------------code---------------------------#
    // vsInput()
    
    n,a,b,c,d=value()
    ans=0
    
    minSum=a+b+2
    maxSum=a+b+2*n
    
    for mid in range(1,n+1):
        box1=(a+b+mid+1,a+b+mid+n)
        box2=(a+c+mid+1,a+c+mid+n)
        box3=(c+d+mid+1,c+d+mid+n)
        box4=(d+b+mid+1,d+b+mid+n)
    
        minSum=max(box1[0],box2[0],box3[0],box4[0])
        maxSum=min(box1[1],box2[1],box3[1],box4[1])
    
        # print(minSum,maxSum)
        ans+=max(maxSum-minSum+1,0)
    
    print(ans)
    
    
    
    
    
    
    
            
    
    
    
            
            
    
    
    
    
    
    
    