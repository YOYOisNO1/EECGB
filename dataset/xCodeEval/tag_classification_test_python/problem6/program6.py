    import sys
    import math
    
    
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().strip().split()
def SI(): return sys.stdin.readline().strip()
def MIN_INT(): return -1 * sys.maxsize
def MAX_INT(): return sys.maxsize
def prefSum(arr, n):
        P = [0] * (n + 1)
        for k in range(1, n + 1):
            P[k] = P[k - 1] + arr[k - 1]
        return P
    
    
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    
def solve():
        a, b = LI()
        if b == 1:
            print(a-1)
        else:
            print((b-1)*a)
    
    
def main():
        solve()
    
    
    main()