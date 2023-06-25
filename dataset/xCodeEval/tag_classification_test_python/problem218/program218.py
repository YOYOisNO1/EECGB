def program218():
    import sys
    from functools import reduce
    
    n, k = map(int, sys.stdin.readline().split())
    turns = 0
    steps = (k - 1 if k <= n / 2 else n - k) + (n - 1)
    turns += steps
    turns += 2 * (n - 1) + 3
                                             
    
    print(turns)
        
    