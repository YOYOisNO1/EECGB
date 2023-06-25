def read_nums():
        return [int(x) for x in input().split()]
    
    n, m = read_nums()
    seq = read_nums()
    fingers = read_nums()
    
    res = []
    for f in seq:
        if f in fingers:
            res.append(f)
    
    res = [str(x) for x in res]
    
    print(' '.join(res))