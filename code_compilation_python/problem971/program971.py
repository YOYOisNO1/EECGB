    class SegmentTree:
    def __init__(self, data, default=0, func=lambda a,b:gcd(a,b)):
            """initialize the segment tree with data"""
            self._default = default
            self._func = func
            self._len = len(data)
            self._size = _size = 1 << (self._len - 1).bit_length()
    
            self.data = [default] * (2 * _size)
            self.data[_size:_size + self._len] = data
            for i in reversed(range(_size)):
                self.data[i] = func(self.data[i + i], self.data[i + i + 1])
    
    def __delitem__(self, idx):
            self[idx] = self._default
    
    def __getitem__(self, idx):
            return self.data[idx + self._size]
    
    def __setitem__(self, idx, value):
            idx += self._size
            self.data[idx] = value
            idx >>= 1
            while idx:
                self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
                idx >>= 1
    
    def __len__(self):
            return self._len
    
    def query(self, start, stop):
            if start == stop:
                return self.__getitem__(start)
            stop += 1
            start += self._size
            stop += self._size
    
            res = self._default
            while start < stop:
                if start & 1:
                    res = self._func(res, self.data[start])
                    start += 1
                if stop & 1:
                    stop -= 1
                    res = self._func(res, self.data[stop])
                start >>= 1
                stop >>= 1
            return res
    
    def __repr__(self):
            return "SegmentTree({0})".format(self.data)
    
    
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
    from bisect import bisect_right, bisect_left
    from fractions import Fraction
    
def pre(s):
        n = len(s)
        pi=[0]*n
        for i in range(1,n):
            j = pi[i-1]
            while j and s[i] != s[j]:
                j = pi[j-1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        return pi
    
def prod(a):
        ans = 1
        for each in a:
            ans = (ans * each)
        return ans
    
    from math import gcd
def lcm(a,b):return a*b//gcd(a,b)
    
def binary(x, length=16):
        y = bin(x)[2:]
        return y if len(y) >= length else "0"*(length - len(y)) + y
    
def sumrange(a,b):
        return a*(b-a+1) + (b-a)*(b-a+1)//2
    
    for _ in range(1):
        #a, k = map(int, input().split())
        a, b, c, d =  map(int, input().split())
        if (b-a)*(c-b)*(d-c) <= 100000:
            ans = 0
            for i in range(a,b+1):
                for j in range(b,c+1):
                    for k in range(c, d+1):
                        if i+j > k and i+k > j and j+k > i:
                            ans += 1
            print(ans)
            continue
        #x, y =  map(int, input().split())
        #a = list(map(int, input().split()))
        #sm = sum(a)
        #for i in range(n):
        #s = input()
        #print("YES" if s else "NO")
        ans = 0
        for i in range(a, b+1):
            if i + b > d:
                ans += (d-c+1)*(c-b+1)
                #print("Here")
            elif i + b == d:
                ans += (i+b-c) + (d-c+1)*(c-b)
            elif i + c <= d:
                #print(i+b, i+c, sumrange(3,4))
                ans += sumrange(i+b, i+c) - c*(c-b+1)
            else:
                mid = d-i
                its = mid - b + 1
                ans += sumrange(i+b, i+b+its-1) - c*its
                ans += (d-c+1)*(c-b+1-its)
        print(max(ans, 0))
    
    
     