    import sys
    import re
    import math
    
def foo(n, R, r):
        if R < r:
            return False
        if n == 1:
            return True
        if r == R:
            return False
    
        if r == R - r:
            return n <= 2
    
        if r > R - r:
            return False
    
        a = math.asin(float(r) / (R - r)) * 2.0
        return 2.0 * math.pi + 1e-9 >= a * n
    
    n, R, r = map(int, input().split())
    print(['NO',) 'YES'][foo(n, R, r)]