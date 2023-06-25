    from __future__ import division
    from sys import stdin, stdout
    from itertools import permutations
    from copy import copy
    
    rint = lambda: int(stdin.readline())
    rints = lambda: [int(x) for x in stdin.readline().split()]
    
    
def solve():
        global ans
        ix1, ix2, cur, a1, b1 = 0, 0, 0, copy(a), copy(b)
    
        while ix1 < 3 and ix2 < 3:
            mi = min(a1[x[ix1]], b1[y[ix2]])
            cur += mi*((x[ix1], y[ix2]) in win)
    
            a1[x[ix1]] -= mi
            b1[y[ix2]] -= mi
    
            if a1[x[ix1]] == b1[y[ix2]]:
                ix1 += 1
                ix2 += 1
            elif a1[x[ix1]] > b1[y[ix2]]:
                ix2 += 1
            else:
                ix1 += 1
    
        ans = [min(ans[0], cur), max(ans[1], cur)]
    
    
    n, a, b, ans = int(input()), rints(), rints(), [float('inf'), 0]
    win = {(0, 1), (1, 2), (2, 0)}
    
    for x in permutations([0, 1, 2], 3):
        for y in permutations([0, 1, 2], 3):
            solve()
    
    print('%d %d' % (ans[0], ans[1]))