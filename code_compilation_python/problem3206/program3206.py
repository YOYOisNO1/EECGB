def program3206():
    import sys
    from math import ceil
    
    input = sys.stdin.readline
    
    n, h, m = map(int, input().split())
    
    houses = [h for i in range(n+1)]
    
    for i in range(m):
        l, r, x = map(int, input().split())
        for j in range(l, r+1):
            houses[j] = min(houses[j], x)
        
    houses.pop(0)
    
    print(sum([x*x for x in houses]))