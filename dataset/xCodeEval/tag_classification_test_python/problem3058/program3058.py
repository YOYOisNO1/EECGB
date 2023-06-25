    import sys, math
def rs():
        return sys.stdin.readline().strip()
def ri():
        return int(sys.stdin.readline().strip())
def ras():
        return list(sys.stdin.readline().strip())
def rai():
        return map(int,sys.stdin.readline().strip().split())
def raf():
        return map(float,sys.stdin.readline().strip().split())
    
def solve():
        a1,a2,a3,a4,a5,a6 = rai()
        return (a1 + a2 + a6)**2 - a2**2 - a4**2 - a6**2
    
    print(solve())