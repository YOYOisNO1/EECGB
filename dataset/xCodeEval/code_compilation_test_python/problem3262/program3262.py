def program3262():
    n = int(input())
    
    xs = set()
    ys = set()
    for i in range(n)
        x, y = map(int, input().split())
        xs.add(x)
        ys.add(y)
    
    if len(xs) > 1 and len(ys) > 1:
        dx = max(xs) - min(xs)
        dy = max(ys) - min(ys)
        print dx*dy
    
    else:
        print -1