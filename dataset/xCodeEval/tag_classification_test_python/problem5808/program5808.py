def program5808():
    import heapq
    import sys
    import bisect
    from collections import defaultdict, Counter
    from itertools import product
    
    
    n = input()
    arr = list(map(int, input().split()))
    
    m = min(arr)
    if sum([a>m for a in arr]) >= len(arr)/2:
        print('Alice')
    else:
        print('Bob')