    import string
    from collections import deque
    from math import comb
    from functools import lru_cache
    
    DEBUG = 0
    
def main():
        @lru_cache(400*2*2)
    def search(n, l_on, r_on):
            nonlocal M
            if n == 0: return 1
            if l_on and r_on and n == 1: return 1
            if n == 1: return 1
            if r_on and not l_on: return search(n, r_on, l_on)
    
            total = 0
            for i in range(n):
                total += search(n=i, l_on=l_on, r_on=True) * search(n=n-i-1, l_on=True, r_on=r_on) * comb(n-1, i) % M
            # print(l_on,  n, r_on, '=>', total)
            return total
    
        # T = Input.read_typed(int)[0]
        T = 1
        while T:
            n, M = Input.read_typed(int)
    
            print(search(n, False, False) % M)
            T -= 1 
    
    
    # Helper classes
    class Input:
    def __init__(self):
            pass
    
        @staticmethod
    def read_typed(cls):
            return list(map(cls, input().split()))
    
        @staticmethod
    def read():
            return input()
    
    class Debug():
    def __init__(self):
            import sys
            sys.stdout = open('output.out', 'w')
            sys.stdin = open('input.in', 'r')
    
    def __delete__(self):
            sys.stdout.close()
            sys.stdin.close()
    
def run():
        if DEBUG: _ = Debug()
        main()
    
    run()