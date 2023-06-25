def program89():
    n, b, p = map(int, input().split())
    
    nt = n*p
    nb = (2*b*(n-1))+(n-1)
    
    if n == 1:
        nb = b
        
    print nb, nt    