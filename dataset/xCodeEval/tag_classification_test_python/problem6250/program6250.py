    from Queue import * # Queue, LifoQueue, PriorityQueue
    from bisect import * #bisect, insort
    from datetime import * 
    from collections import * #deque, Counter,OrderedDict,defaultdict
    #set([]) 
    import calendar
    import heapq
    import math
    import copy
    import itertools
    import string
    myread = lambda : map(int,input().split())
def solver():
        N = input()
        MOD = 1000000007
        n = pow(2,N,MOD)
        ans = (n * (n+1) /2) % MOD
        print(ans)
    if __name__ == "__main__":
        solver()
        