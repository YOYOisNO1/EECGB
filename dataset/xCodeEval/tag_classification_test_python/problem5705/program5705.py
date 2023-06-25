    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import sys
    import math
    
    
def float_equality(a, b):
        EPS = 0.000001
        return abs(a-b) <= EPS
    
    if __name__ == '__main__':
        x, y, n = map(int, sys.stdin.readline().strip().split())
    
        min_diff = None
        min_a, min_b = None, None
        for b in xrange(1, n + 1):
            closer = float(x * b) / float(y)
            list_a = [int(math.floor(closer)), int(math.ceil(closer))]
    
            for a in list_a:
    
                diff = abs(float(x*b - y*a)/float(y*b))
    
                if min_diff is None or diff - min_diff < -0.0000000000000001:
                    min_diff = diff
                    min_a, min_b = a, b
    
                if float_equality(diff, min_diff):
                    if b < min_b or (b == min_b and a < min_a):
                        min_diff = diff
                        min_a, min_b = a, b
    
    
        print("{}/{}").format(min_a, min_b)