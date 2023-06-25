def program6398():
    n, k = map(int, input().split())
    min_h = 1
    max_h = 1
    if n == k or k == 0:
        min_h = 0
        max_h = 0
    elif k > n/3:
        max_h = n - k
    else:
        max_h = 2*k
    print(min_h,) max_h
    
    
    
    
    # oxooxo
    # ooxooxo