def program3545():
        from itertools import *
        n, k = map(int, input().split())
        a = [input() for _ in range(n)]
        idx = list(permutations(range(k), k))
        res = 99999999
        for j in idx:
            b = [int(''.join(x[i] for i in j)) for x in a]
            diff = max(b) - min(b)
            if diff < res: res = diff
        print res