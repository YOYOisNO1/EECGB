     
    # Rhythem Jain
    # Date: 24.09.20
    
    
    from __future__ import division, print_function
    import os,sys
    from io import BytesIO, IOBase
    
    from collections import deque, Counter, OrderedDict,defaultdict
    # from binarytree import tree,heap,bst,Node
    # from Queue import LifoQueue
    #from heapq import nsmallest, nlargest, heapify,heappop ,heappush, heapreplace
    #from math import log,sqrt,factorial,cos,tan,sin,radians
    #from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
    #from decimal import *
    #import threading
    from itertools import permutations,combinations
    # Copy 2D list  m = [x[:] for x in mark] .. Avoid Using Deepcopy 
    
    if sys.version_info[0] < 3:
        from __builtin__ import xrange as range
        from future_builtins import ascii, filter, hex, map, oct, zip
    
def ii():  return int(input())
def si():  return input()
def mi():  return map(int,input().strip().split())
def msi(): return map(str,input().strip().split())
def li():  return list(mi())
     
def dmain():
        sys.setrecursionlimit(1000000)
        threading.stack_size(1024000)
        thread = threading.Thread(target=main)
        thread.start()
        
    from collections import deque, Counter, OrderedDict,defaultdict
    from math import *
    from itertools import permutations,combinations
     
    abc='abcdefghijklmnopqrstuvwxyz'
    abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    mod=1000000007
    vow=['a','e','i','o','u','A','E','I','O','U']
    dx,dy=[-1,1,0,0],[0,0,1,-1]
def getKey(item): return item[1] 
def sort2(l):return sorted(l, key=getKey,reverse=True)
def d2(n,m,num):return [[num for x in range(m)] for y in range(n)]
def isPowerOfTwo (x): return (x and (not(x & (x - 1))) )
def decimalToBinary(n): return bin(n).replace("0b","")
def ntl(n):return [int(i) for i in str(n)]
def ncr(n,r): return factorial(n)//(factorial(r)*factorial(max(n-r,1)))
     
def ceil(x,y):
        if x%y==0:
            return x//y
        else:
            return x//y+1
     
def powerMod(x,y,p):
        res = 1
        x %= p
        while y > 0:
            if y&1:
                res = (res*x)%p
            y = y>>1
            x = (x*x)%p
        return res
    
def expo(x,y,m):
        if y==0:
            return 1
        elif y%2==0:
            return expo((x*x)%m,y/2,m)
        else:
            return x*expo((x*x)%m,(y-1)/2,m)%m
    
def gcd(a, b):
        if a==0:
            return b,0,1
        gc,x1,y1=gcd(b%a,a)
        x=y1-(b//a)*x1
        y=x1 
        return gc,x,y
    
def sieve(n):
        arr=[True]*(n+1)
        arr[0]=False
        arr[1]=False
        for i in range(4,n+1,2):
            arr[i]=False
        for i in range(3,int(sqrt(n))+1,2):
            if arr[i]==True:
                for j in range(i*i,n+1,i):
                    arr[j]=False
        return arr
    
def modInverse(x,y):
        gc,x1,y1 = gcd(x,y)
        return (y1+y)%y
    
def isPrime(n) : 
        if (n <= 1) : return False
        if (n <= 3) : return True
        if (n % 2 == 0 or n % 3 == 0) : return False
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                return False
            i = i + 6
        return True
     
def read():
        sys.stdin  = open('input.txt', 'r')  
        sys.stdout = open('output.txt', 'w') 
    
def main():
        n=ii()
        a,b,c=mi()
        d,e,f=mi()
        val=min(a,e)+min(b,f)+min(c,d)
        val1=max(0,a-d-f)+max(b-e-d,0)+max(0,c-e-f)
    
        print(val1,val)
    
    
    
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
    
    
def print(*args, **kwargs):
        """Prints the values to a stream, or to sys.stdout by default."""
        sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
        at_start = True
        for x in args:
            if not at_start:
                file.write(sep)
            file.write(str(x))
            at_start = False
        file.write(kwargs.pop("end", "\n"))
        if kwargs.pop("flush", False):
            file.flush()
    
    
    if sys.version_info[0] < 3:
        sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
    else:
        sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    
    
    if __name__ == "__main__":
        main()