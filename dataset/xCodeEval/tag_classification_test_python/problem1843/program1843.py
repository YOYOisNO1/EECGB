    from collections import defaultdict as dd, deque as dq
    import math, string
    
    import sys
    
def getInts():
        return [int(s) for s in input().split()]
    
def getInt():
        return int(input())
    
def getStrs():
        return [s for s in input().split()]
    
def getStr():
        return input()
    
def listStr():
        return list(input())
    
    MOD = 10**9+7
    
    """
    11 can become 10 or 01
    10 can become 11
    01 can become 11
    00 stays 00
    So essentially 10-01-11 are all interchangeable
    """
    
def solve():
        A, B = getInts()
        ans = 0
        if A > B: B, A = A, B
        #A <= B
        if B % A > 0:
            return -1
        X = B//A
        while X % 2 == 0:
            X //= 2
            ans += 1
        while X % 3 == 0:
            X //= 3
            ans += 1
        if X > 1:
            return -1
        return ans
        
        
    #for _ in range(getInt()):
    print(solve())