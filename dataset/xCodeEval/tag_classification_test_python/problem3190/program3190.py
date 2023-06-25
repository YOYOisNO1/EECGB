    #!/usr/bin/env python
    import os
    import sys
    from io import BytesIO, IOBase
    import threading 
    from bisect import bisect_right
    from math import gcd,log
    from collections import Counter,defaultdict,deque
    from pprint(import) pprint(from) itertools import permutations 
    from bisect import bisect_right
    from random import randint as rti 
    # import deque
    
    
def is_pos(arr):
        n=len(arr)
        total=sum(arr)
        if total%2:
            return False
        MX=total//2+1
        pos=[0]*MX
        pos[0]=1
        for i in range(n): 
            for j in range(MX-1-arr[i],-1,-1):
                pos[j+arr[i]]|=pos[j]
            if pos[MX-1]:
                return True
        return False
    
    
    
    MOD=10**9+7
def main():
        n=int(input())
        arr=list(map(int,input().split()))
        total=sum(arr)
    
        if total%2 or (not is_pos(arr)):
            print(0)
            return 
        for i in range(n):
            brr=arr[:i]+arr[i+1:]
            if not is_pos(brr):
                print(1)
                print(i+1)
                return 
    
    
    
    
    
            
    
    
    
    
        
    
        
    
    
    
    
    
    
    
    
            
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
    
        for _ in range(1): 
            main()
    
    
    