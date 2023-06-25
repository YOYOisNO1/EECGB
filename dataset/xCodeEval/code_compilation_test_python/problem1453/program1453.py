def program1453():
    
    	'''input
    5
    1 2 3 4 5
    
    
    '''
    
    RI = lambda : [int(x) for x in input().split()]
    rw = lambda : input().strip()
    
    
    n = input()
    A= RI()
    
    print (A[2]^(min(A))) + 2