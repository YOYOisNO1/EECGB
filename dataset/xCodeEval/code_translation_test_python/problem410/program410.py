    #------------------------template--------------------------#
    import os
    import sys
    from math import *
    from collections import *
    # from fractions import *
    # from heapq import*
    from bisect import *
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
    M=10**9+7
    EPS=1e-6
def Ceil(a,b): return a//b+int(a%b>0)
def value():return tuple(map(int,input().split()))
def array():return [int(i) for i in input().split()]
def Int():return int(input())
def Str():return input()
def arrayS():return [i for i in input().split()]
    
    
    #-------------------------code---------------------------#
    # vsInput()
    
    
def Waiting(over,pos,d):
    
        # print(over)
        over=over//t1
    
        if(d==1):
            cur=initial+over
            if(cur>=s):
                d=-1
                cur=s-(cur-s)
        else:
            cur=initial-over
            if(cur<=0):
                d=1
                cur*=-1
    
        # print(cur)
        ans=0
    
        if(d!=my_dir):
            if(d==1):
                ans+=(s-cur)
                d=-1
                cur=s
            else:
                ans+=(cur)
                d=1
                cur=0
        
        # print(cur,pos)
    
        if(d==1):
            if(cur<=pos): ans+=(pos-cur)
            else: ans+=s+pos+(s-cur)
        else:
            if(cur>=pos): ans+=abs(pos-cur)
            else: ans+=cur+s+(s-pos)
    
        return ans*t1
    
    
    
    s,x1,x2=value()
    t1,t2=value()
    initial,d=value()
    
    my_dir=1
    if(x2<x1):my_dir=-1
    
    ans=abs(x2-x1)*t2
    
    
    for i in range(min(x1,x2),max(x2,x1)+1):
    
        x1_to_i=abs(i-x1)*t2
        waiting_at_i=Waiting(x1_to_i,i,d)
        i_to_x2=abs(x2-i)*t1
    
        if(i==x2): waiting_at_i=0
    
        # print(i,'-->' ,x1_to_i, waiting_at_i, i_to_x2)
    
        ans=min(x1_to_i+waiting_at_i+i_to_x2,ans)
    
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
    
    
    
        
            
    
       
    
    
    
    
    
    
    
    
    
    
    