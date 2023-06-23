def program4465():
    import sys
    
    a,b,N = map(int,input().split())
    
    if N == 1:
        print a
        sys.exit(0)
    if N == 2:
        print b
        sys.exit(0)
    
    x = 2
    while (x < N):
        temp = b
        b += a
        a = temp
        
        x += 1
        if x == N: print b
        