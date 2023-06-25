    from collections import deque, defaultdict as ddic, Counter
    from itertools import combinations, permutations, product, groupby
    import heapq, bisect
    from fractions import Fraction, gcd
    MOD = 10**9 + 7
    rr = input
    rri = lambda: int(input())
    rrm = lambda: map(int, input().split())
    
    ###
    
def solve(N, A):
        return A.count(min(A)) <= N / 2
    
    print("Alice") if solve(rri(), rrm()) else "Bob"