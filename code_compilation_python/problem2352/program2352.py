def program2352():
    '''
    6
    10 2 3 5 4 2
    '''
    lens = int(input())
    cols = 0
    arrs = [int(x) for x in input(),split()]
    while arrs:
        arrs = [x for x in arrs if x/min(arrs) == 0]
        cols += 1
    print(cols)    
        