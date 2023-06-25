    import gc
    import heapq
    import itertools
    import math
    import sqlite3
    from collections import Counter, deque, defaultdict
    from sys import stdout
    import time
    from math import factorial, log, gcd
    import sys
    from decimal import Decimal
    import threading
    from heapq import *
    from fractions import Fraction
    
    
def S():
        return sys.stdin.readline().split()
    
    
def I():
        return [int(i) for i in sys.stdin.readline().split()]
    
    
def II():
        return int(sys.stdin.readline())
    
    
def IS():
        return sys.stdin.readline().replace('\n', '')
    
    
def main():
        n = II()
        max_n = 10 ** 6
        mod = 998244353
        dividers = [1] * (max_n + 1)
        for i in range(2, max_n + 1):
            for j in range(i, max_n + 1, i):
                dividers[j] += 1
    
        dp = [1] * (max_n + 1)
        s = 1
        for i in range(2, max_n + 1):
            dp[i] = (s + dividers[i]) % mod
            s = (dp[i] + s) % mod
        print(dp[n])
    
    
    if __name__ == '__main__':
        # for _ in range(II()):
        #     main()
        main()