    import string
    from collections import deque, Counter
    from math import comb
    from functools import lru_cache
    
    DEBUG = 0
    
def main():
        # @lru_cache(400*2*2)
    # def search(n, l_on, r_on):
        #     nonlocal M
        #     if n == 0: return 1
        #     if l_on and r_on and n == 1: return 1
        #     if n == 1: return 1
        #     if r_on and not l_on: return search(n, r_on, l_on)
    
        #     total = 0
        #     for i in range(n):
        #         total += search(n=i, l_on=l_on, r_on=True) * search(n=n-i-1, l_on=True, r_on=r_on) * comb(n-1, i) % M
        #     # print(l_on,  n, r_on, '=>', total)
        #     return total
    
    
        @lru_cache(400 * 400)
    def search(total, manual):
            nonlocal M
            if manual == 0: return 1 if total == 1 else 0
            if total == manual: return pow(2, total-1, mod=M)
            if total > manual*2: return 0
            if total < manual: return 0
    
            v = 0
            for l in range(1, manual):
                v += search(total-l-1, manual-l) * pow(2, l-1, mod=M) * comb(manual, l) % M
            return v % M
    
        T = 1
        while T:
            n, M = Input.read_typed(int)
    
            N = n
            c = 0
            for i in range(1, n+1):
                c += search(n, i)
                # print(n, i)
                # print(search(n, i))
            print(c % M)
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