    # cook your dish here
    from sys import stdin, stdout
    import math
    from itertools import permutations, combinations
    from collections import defaultdict
    from bisect import bisect_left
     
def L():
        return list(map(int, stdin.readline().split()))
     
def In():
        return map(int, stdin.readline().split())
     
def I():
        return int(stdin.readline())
     
    P = 1000000007
    for t in range(I()):
        arr = L()
        arr.sort()
        arr[0], arr[-1] = arr[-1], arr[0]
        print(*arr)