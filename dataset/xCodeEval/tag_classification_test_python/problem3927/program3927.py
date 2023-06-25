    from sys import stdin
    from collections import defaultdict
    from itertools import combinations
    from math import log, ceil
    
    
def finish():
        print('YES')
        exit()
    
    
    w, m = map(int, stdin.readline().split())
    all = [pow(w, x) for x in range(int(ceil(log(10 ** 9, w))) + 1)]
    
    if w in [2, 3] or m in all:
        print('YES')
    else:
        mem1, mem2 = {m}, set()
    
        for i in range(1, len(all)):
            for com in combinations(all, i):
                su = sum(com)
                mem1.add(su + m)
                mem2.add(su)
    
        print('NO' if not mem2.intersection(mem1) else 'YES')