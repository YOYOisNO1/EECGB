    import math
    import functools
    
    
    @functools.lru_cache(maxsize=None)
def factorial(n):
        return math.factorial(n)
    
    
    @functools.lru_cache(maxsize=None)
def binomial(k, n):
        return factorial(n) // (factorial(k) * factorial(n - k))
    
    
def P(k, n, m):
        return k ** 2 * binomial(k, m) * binomial(n - k, n * m - m)
    
    
def solve(n, m):
        return sum(P(k, n, m) for k in range(1, min(n, m) + 1)) / binomial(n, m * n) / n
    
    
    if __name__ == '__main__':
        n, m = map(int, input().split())
    
        print(solve(n, m))