def program563():
    '''input
    3 3
    '''
    
    # a + b = a^b + (a&b)*2
    s, x = map(int, input().split())
    d = s-x  # d/2 is a&b
    
    if d%2 or (d/2 & x):
        print(0)
    else:
        print(2**bin(x).count('1')) - (0 if d else 2)