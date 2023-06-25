def program1328():
    
    A = map(int, input().split())
    B = map(int, input().split())
    C = map(int, input().split())
    
    AB = (B[0] - A[0], B[1] - A[1])
    AC = (C[0] - A[0], C[1] - A[1])
    
    p = AB[0] * AC[1] - AC[0] * AB[1]
    
    if p == 0:
        print('TOWARDS')
    elif p > 0:
        print('LEFT')
    elif p < 0:
        print('RIGHT')
    else:
        raise ValueError