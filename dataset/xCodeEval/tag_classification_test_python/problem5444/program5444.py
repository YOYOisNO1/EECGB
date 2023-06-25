def program5444():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    from collections import defaultdict
    
    count = defaultdict(int)
    
    for i in a:
        count[i] += 1
    
    for d in range(100, 0, -1):
        p = 0
        c = count.copy()
    
        for i in range(1, 101):
            p += c[i] // d
    
        if p >= n:
            print(d)
            exit()
    
    print(0)