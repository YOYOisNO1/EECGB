def program4257():
    n, m = map(int, input().split())
    b = map(int, input().split())
    
    off = [''] * (n + 1)
    for x in b:
        for i in range(x, n + 1):
            if not off[i]:
                off[i] = x
    
    print(' '.join(map(str, off[1:])))