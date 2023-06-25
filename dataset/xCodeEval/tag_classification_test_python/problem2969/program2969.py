def program2969():
    import sys
    import random
    import functools
    import re
    import itertools
    import math
    import copy
    import bisect
    import Queue
    from collections import Counter
    
    n = int(sys.stdin.readline())
    sizes = [int(_) for _ in sys.stdin.readline().split()]
    
    sol = (0, 0)
    
    for x in reversed(sizes):
        my, other = sol
        sol = max((my, other + x), (x + other, my))
    
    print(sol[1],) sol[0]