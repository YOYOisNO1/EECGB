def program5644():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    n, m = min(n,m), max(n,m)
    if n == 1:
        print(m)
    elif n == 2:
        print([0,2,4,4][m%4]+(m//4)*4)
    else:
        print((n*m+1)//2)
    
    #1 : 1 2 3 4 5 6 7 8
    #2 : 2 4 4 4 6 8 8 8
    #3 : 3 4 5 6 8 9    
    #4 : 4 4 6 8 10      
    #5 : 5 6 8 10        
    #6 : 6 8 9          
    #7 : 7 8            
    #8 : 8 8      