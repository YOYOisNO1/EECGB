    # -*- coding: utf-8 -*-
    from itertools import imap
    from heapq import merge
    from bisect import bisect
    
    
def readline(): return imap(int, input().split())
    
    
    class Solved(Exception):
        pass
    
    
def get_values(a, m):
        values = [(0, 1)]
        for v in a:
            new_values1, new_values2 = [], []
            for (x, y) in values:
                x1, y1 = x + v, y + v
                if x1 < m:
                    if y1 < m:
                        new_values1.append((x1, y1))
                    else:
                        print(m - 1)
                        raise Solved
                else:
                    new_values2.append((x1 - m, y1 - m))
    
            new_values = []
            hx, hy = 0, 1
            for pair in merge(values, new_values1, new_values2):
                if hy >= pair[0]:
                    hy = pair[1]
                else:
                    new_values.append((hx, hy))
                    hx, hy = pair
            values = new_values + [(hx, hy)]
        return values
    
    
def main():
        n, m = tuple(readline())
        a = filter(bool, (x % m for x in readline()))
    
        mid = (n + 1) >> 1
        a1, a2 = a[:mid], a[mid:]
    
        try:
            v1, v2 = get_values(a1, m), get_values(a2, m)
        except Solved:
            return
    
        ans = max(max(v1)[1] - 1, max(v2)[1] - 1)
    
        for (x, y) in v2:
            if ans == m - 1:
                break
            idx = bisect(v1, (m - x, 0))
            if not idx:
                break
            y1 = v1[idx - 1][1]
            assert y1 - 1 < m - x
            ans = max(ans, m - 1 if y1 - 1 >= m - y else y - 1 + y1 - 1)
    
        print(ans)
    
    
    main()