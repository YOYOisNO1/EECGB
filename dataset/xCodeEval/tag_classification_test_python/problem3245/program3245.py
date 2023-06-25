    """
        Satwik_Tiwari ;) .
        12th july , 2020  - Sunday
    """
    
    #===============================================================================================
    #importing some useful libraries.
    from __future__ import division, print_function
    
    from fractions import Fraction
    import sys
    import os
    from io import BytesIO, IOBase
    
    from itertools import *
    import bisect
    from heapq import *
    from math import *
    from collections import deque
    from collections import Counter as counter  # Counter(list)  return a dict with {key: count}
    from itertools import combinations as comb # if a = [1,2,3] then print(list(comb(a,2))) -----> [(1, 2), (1, 3), (2, 3)]
    from itertools import permutations as permutate
    from bisect import bisect_left as bl
    #If the element is already present in the list,
    # the left most position where element has to be inserted is returned.
    from bisect import bisect_right as br
    from bisect import bisect
    #If the element is already present in the list,
    # the right most position where element has to be inserted is returned
    
    #==============================================================================================
    
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
    
    # inp = lambda: sys.stdin.readline().rstrip("\r\n")
    
    #===============================================================================================
    #some shortcuts
    
    mod = 1000000007
def inp(): return sys.stdin.readline().rstrip("\r\n") #for fast input
def out(var): sys.stdout.write(str(var))  #for fast output, always take string
def lis(): return list(map(int, inp().split()))
def stringlis(): return list(map(str, inp().split()))
def sep(): return map(int, inp().split())
def strsep(): return map(str, inp().split())
# def graph(vertex): return [[] for i in range(0,vertex+1)]
def zerolist(n): return [0]*n
def nextline(): out("\n")  #as stdout.write always print(sring.)
def testcase(t):
        for p in range(t):
            solve()
def printlist(a) :
        for p in range(0,len(a)):
            out(str(a[p]) + ' ')
def lcm(a,b): return (a*b)//gcd(a,b)
def power(a,b):
        ans = 1
        while(b>0):
            if(b%2==1):
                ans*=a
            a*=a
            b//=2
        return ans
def ncr(n,r): return factorial(n)//(factorial(r)*factorial(max(n-r,1)))
def isPrime(n) : # Check Prime Number or not
        if (n <= 1) : return False
        if (n <= 3) : return True
        if (n % 2 == 0 or n % 3 == 0) : return False
        i = 5
        while(i * i <= n) :
            if (n % i == 0 or n % (i + 2) == 0) :
                return False
            i = i + 6
        return True
    
    #===============================================================================================
    # code here ;))
def dist(x0,y0,x1,y1):
        return (abs(x0-x1) + abs(y0-y1))
    
def solve():
        x0,y0,a1,a2,b1,b2 = sep()
        xs,ys,t = sep()
        points = []
        f = False
        if(dist(xs,ys,x0,y0)<=t):
            points.append([x0,y0])
        while(True):
            x = (a1*x0)+b1
            y = (a2*y0)+b2
            if(dist(xs,ys,x,y) <=t):
                points.append([x,y])
            else:
                if(x>xs and y>ys):
                    break
            x0,y0 = x,y
        if(len(points) == 0):
            print(0)
            return
    
        # print(points)
        left = []
        right = []
        d = []
        for i in range(len(points)):
            d.append(dist(xs,ys,points[i][0],points[i][1]))
        # print(d)
    
        ind = d.index(min(d))
        # print(ind)
        ans = 1
        for i in range(0,ind+1):
            for j in range(ind+1,len(d)):
                if(d[i] + dist(points[i][0],points[i][1],points[j][0],points[j][1]) <= t):
                    ans = max(ans,(ind-i+1)+(j-ind))
                else:
                    break
        for i in range(ind,len(d)):
            for j in range(0,ind):
                if(d[i] + dist(points[i][0],points[i][1],points[j][0],points[j][1])<=t):
                    ans = max(ans,(i-ind+1)+(ind-j))
        print(ans)
    
    
    
    
        # for i in range(len(points)):
        #     if(points[i][0]<=xs):
        #         left.append(points[i])
        # for i in range(len(points)):
        #     if(points[i][0]>xs):
        #         right.append(points[i])
        # print(right)
        # print(left)
        # if(left[len(left)-1] == [xs,ys]):
        #     ans=  max(len(left),len(right)+1)
        # else:
        #     ans = max(len(left),len(right))
        # lefttimes = [0]*len(left)
        # righttimes = [0]*len(right)
        #
        # for i in range(len(left)):
        #     lefttimes[i] = dist(xs,ys,left[i][0],left[i][1])
        # for i in range(len(right)):
        #     righttimes[i] = dist(xs,ys,right[i][0],right[i][1])
        # for i in range(len(left)):
        #     timeleft = t - (lefttimes[i] + dist(left[i][0],left[i][1],right[i][0],right[i][1]))
        #     if(timeleft <=0):
        #         if(i==0 and timeleft == 0):
        #             ans = max(ans,len(left)+1)
        #         continue
        #     else:
        #         ind = bl(righttimes,timeleft)
        #         if(righttimes[ind] == timeleft):
        #             ans = max(ans,ind+1)
        #         else:
        #             ans = max(ans,ind)
        # for i in range(len(right)):
        #     timeleft = t - (righttimes[i])*2
        #     if(timeleft<=0):
        #         continue
        #     else:
        #         ind = bl(lefttimes,timeleft)
        #         if(lefttimes[ind] == timeleft):
        #             ans = max(ans,ind+1)
        #         else:
        #             ans = max(ans,ind)
        # print(ans)
    
    
    
    
    
    
    testcase(1)
    # testcase(int(inp()))
    
    
    
    
    
    
    
    
    
    
    
    
    