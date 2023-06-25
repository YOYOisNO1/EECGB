def program1594():
    n, k = map(int, input().split())
    min_h = 1
    max_h = 0
    
    if k > n/3:
        max_h = n - k
    else if k == n/3:
        max_h = n - k 
        max_h += n % 3
    else:
        max_h = 2*k
    print min_h, max_h
    
    
    
    
    # oxooxo
    # ooxooxo