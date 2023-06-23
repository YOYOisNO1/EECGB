    from __future__ import print_function, division
    import os
    import sys
    from functools import reduce
    from io import BytesIO, IOBase
    
    range = xrange
    input = input
    
    sys.stdout, stream = IOBase(), BytesIO()
    sys.stdout.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
    sys.stdout.write = lambda s: stream.write(s.encode())
    
    input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    MAGIC = float(2**52+2**51)
    
def modder(x,y):
        return x - y*((x/y + MAGIC) - MAGIC)
    
def gcd(x, y):
        """ greatest common divisor of x and y """
        while y:
            x, y = y, modder(x,y)
        return abs(x)
    
def main():
        n, k = [float(x) for x in input().split()]
        nk = n*k
        a, b = [float(x) for x in input().split()]
    
        mini = gcd(nk, (a+b)%k)
        maxi = gcd(nk, (a+b)%k)
    
        for li in [(a + b) % k, (max(a,b) - min(a,b)) % k]:
            while li < nk:
                res = gcd(nk, li)
                mini = min(mini, res)
                maxi = max(maxi, res)
                li += k
    
        print(*[int(nk)//int(maxi), int(nk)//int(mini)])
    
    
    if __name__ == '__main__':
        main()