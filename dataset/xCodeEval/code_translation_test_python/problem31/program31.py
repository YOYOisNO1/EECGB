    # DON'T USE PYTHON FOR RECURSION
    # TRY PYPY
    import math
    import operator
    import sys
    from collections import Counter, defaultdict
    from math import ceil, floor, pi, sin, sqrt
    from sys import exit, stdin, stdout
    
    
def main():
        # stdin = open('.in')
        n, m = map(int, stdin.readline().strip().split(' '))
        ans = 0
        for a in range(1001):
            for b in range(1001):
                ans += a * a + b == n and a + b * b == m
        print(ans)
    
    
    main()