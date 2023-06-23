    import sys
    import math
    
    
def theta(R, r):
        return 2 * math.asin(1.0 * r / (R - r))
    
def can(n, R, r):
        if r >= R:
            return r == R and n == 1
        else if 2 * r >= R:
            return 2 * r == R and n == 2 or n == 1
        else:
            return theta(R, r) * n <= 2 * math.pi + 1e-6
    
    n, R, r = [int(s) for s in sys.stdin.readline().split(' ')]
    print ("YES" if can(n, R, r) else "NO")