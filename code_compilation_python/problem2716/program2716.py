    import functools
    import sys
    
    _MODULO = 10 ** 8
    n1, n2, k1, k2 = map(int, input().split())
    
    # t = [[[[[0] for _ in range(k2)] for _ in range(k1)] for _ in range(n2)] for _ in range(n1)]
    #
    # t[0][0][0][0] = 1
    
    sys.setrecursionlimit(100 * 100 * 10 * 10)
    
    
    @functools.lru_cache(None)
def get(n1, n2, a, b):
        s = (n1, n2, a, b)
        if (n1 == a and n2 == 0) or (n1 == 0 and n2 == b):
            return 1
        if 0 < a <= n1:
            return sum(get(n1 - a, n2, 0, k) for k in range(1, k2 + 1)) % _MODULO
        if 0 < b <= n2:
            return sum(get(n1, n2 - b, k, 0) for k in range(1, k1 + 1)) % _MODULO
        return 0
    
    
    r = 0
    for i in range(1, k1 + 1):
        r += get(n1, n2, i, 0)
    
    for i in range(1, k2 + 1):
        r += get(n1, n2, 0, i)
    
    print(r)