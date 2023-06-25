    from functools import lru_cache
    
    @lru_cache(maxsize=None)
def count_ways(n, k, d):
        if n in (0, d):
            return 1
        if n < d:
            return 0
        return (sum(count_ways(n - i, k, d) for i in range(1, d)) +
                sum(count_ways(n - i, k, 1) for i in range(d, k + 1)))
    
    
    n, k, d = map(int, input().split())
    
    print(count_ways(n, k, d) % 1000000007)