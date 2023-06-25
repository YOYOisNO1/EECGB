    from itertools import combinations, chain
    from math import inf
    
def take(s):
        return sum([abs(next(s) - next(s)) for _ in range(n-1)])
    
    n = int(input())
    wi = sorted(map(int, input().split()))
    minimum = inf
    for lonely_couple in combinations(range(2*n), 2):
        sample = chain(wi[:lonely_couple[0]], wi[lonely_couple[0]+1:lonely_couple[1]], wi[lonely_couple[1]+1:])
        minimum = min(minimum, take(sample))
    print(minimum)
    
    
    
    """
    4
    1 3 4 6 3 4 1000 200
    """