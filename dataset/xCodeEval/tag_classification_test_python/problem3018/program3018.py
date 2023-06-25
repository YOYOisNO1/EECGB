    # -*- coding: utf-8 -*-
    import sys
    from functools import reduce
    from operator import xor
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline
    INF = 2**62-1
    
def read_int():
        return int(input())
    
    
def read_int_n():
        return list(map(int, input().split()))
    
    
def read_float():
        return float(input())
    
    
def read_float_n():
        return list(map(float, input().split()))
    
    
def read_str():
        return input().strip()
    
    
def read_str_n():
        return list(map(str, input().split()))
    
    
def error_print(*args):
        print(*args, file=sys.stderr)
    
    
def mt(f):
        import time
    
    def wrap(*args, **kwargs):
            s = time.time()
            ret = f(*args, **kwargs)
            e = time.time()
    
            error_print(e - s, 'sec')
            return ret
    
        return wrap
    
    
    @mt
def slv(U, V):
        if U == 0 and V == 0:
            print(0)
            return
        if U > V:
            print(-1)
            return
        if U == V:
            print(1)
            print(U)
            return
    
        if U & 1 != V & 1:
            print(-1)
            return
    
        x = U
        y = (V - U) // 2
        if x & y == 0:
            print(2)
            print(x+y, y)
        else:
            print(3)
            print(x, y, y)
    
    
def main():
        U, V = read_int_n()
        slv(U, V)
    
    
    if __name__ == '__main__':
        main()