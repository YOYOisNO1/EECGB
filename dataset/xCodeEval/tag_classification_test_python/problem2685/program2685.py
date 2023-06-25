def program2685():
    p = [tuple(map(int, input().split())) for _ in range(3)]
    xs = sorted([i for i,j in p])
    ys = sorted([j for i,j in p])
    x = set(xs)
    y = set(ys)
    
    if len(x) == 1 or len(y) == 1: print(1)
    elif len(x) == len(y) == 2: print(2)
    elif len(x) == 2 or len(y) == 2:
        if len(x) == 2:
            z = next(j for i,j in p if i != xs[1])
            a, b = sorted([j for i,j in p if i == xs[1]])
            print(3) if a<z<b else 2
        else:
            z = next(i for i,j in p if j != ys[1])
            a, b = sorted([i for i,j in p if j == ys[1]])
            print(3) if a<z<b else 2
    else: print(3)