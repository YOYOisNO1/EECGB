def program657():
    import math
    n, m = map(int, input().split(' '))
    
    a = min(n, 2*m)
    
    # m^2-m-2*n = 0
    #1/2 +- (1 + 8n)^0.5/2
    
    b = math.ceil( 0.5*(1 + pow(1+8*m, 0.5)) )
    if m == 0: b = 0 
    print(n-a, n-b)