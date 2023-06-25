def program1503():
    [a, b, r] = [int(x) for x in input().split()]
    
    if min(a, b) < 2*r:
        print('Second')
    else:
        print('First')