    import math
    from collections import Counter
    
    n = int(input())
    g = [0 for i in range(n + 1)]
    prefix_xor = g.copy()
    
    
def in_range(d, k):
        if (2 * k - d * d + d) % (2 * d) != 0:
            return -1
        x = (2 * k - d * d + d) / (2 * d)
        return int(x) if x > 0 else -1
    
    
def mex(arr):
        counter = Counter()
        for i in arr:
            counter[i] += 1
        for i in range(0, len(arr) + 1):
            if counter[i] == 0:
                return i
    
    
def find_move(arr):
        for i in range(0, len(arr)):
            if arr[i] == 0:
                return i
        return -1
    
    
    if n < 3:
        print(-1)
        exit(0)
    for i in range(3, n + 1):
        for_range = range(2, int(math.sqrt(2 * i)) + 1)
        filter_range = [l for l in for_range if in_range(l, i) > 0]
        branches = [prefix_xor[in_range(d, i) + d - 1] ^ prefix_xor[in_range(d, i) - 1] for d in filter_range]
        g[i] = mex(branches)
        prefix_xor[i] = prefix_xor[i - 1] ^ g[i]
        if i == n:
            print(-1 if g[i] == 0 else filter_range[find_move(branches)])