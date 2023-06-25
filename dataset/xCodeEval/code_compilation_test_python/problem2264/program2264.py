    #!/usr/bin/env python3
    import os
    import sys
    from functools import reduce
    from io import BytesIO, IOBase
    
    sys.stdout, stream = IOBase(), BytesIO()
    sys.stdout.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
    sys.stdout.write = lambda s: stream.write(s.encode())
    
    input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    
def gcd(x, y):
        """ greatest common divisor of x and y """
        while y:
            x, y = y, x % y
        return x
    
    import _numpypy
    zero = _numpypy.multiarray.dtype('int64').type(0)
    one = 1 + zero
    
    gcdm = lambda *args: reduce(gcd, args, zero)
    
    lcm = lambda a, b: a * b // gcd(a, b)
    
    lcmm = lambda *args: reduce(lcm, args, one)
    
    
def main():
        n, k = map(float, input().split())
        a, b = map(float, input().split())
    
        min_l = {(a + b) % k, (a - b) % k, (-a + b) % k, (-a - b) % k}
        res = [10**18 + zero, 0]
        for li in min_l:
            while li < n * k:
                x = li if li else n * k
                res = [min(res[0], lcm(x, n * k) // x), max(res[1], lcm(x, n * k) // x)]
                li += k
    
        print(*[int(x) for x in res])
    
    
    if __name__ == '__main__':
        main()