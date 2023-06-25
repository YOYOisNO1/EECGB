def program4546():
    import sys
    input = sys.stdin.readline
    #from collections import deque
    #from bisect import bisect_left, bisect_right
    #import itertools
    #import math
    
    for _ in range(int(input())):
        
    
        n, k = map(int, input().split())
        print(pow(n, k, 1000000007))