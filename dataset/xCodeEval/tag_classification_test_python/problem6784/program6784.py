def program6784():
    #coding=utf8
    '''
    Created on 20160607
    
    @author: ChronoCorax
    '''
    n, k = [int(c) for c in input().split()]
    c = n - 2 * k
    if c < 0: c = 0
    a = n * (n - 1) // 2 - c * (c - 1) // 2
    print(a)