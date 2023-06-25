    INF = 999999999999999999L
    EPS = 1e-12
    
def read():
        return input().strip()
    
def read_ints():
        return map(int,read().split())
    
    n,m = read_ints()
    if n > m:
        n,m = m,n 
        
    if n == 1:
        empty = [0,1,2,3,2,1][m%6]
    elif n == 2:
        if m == 2:
            empty = 4
        elif m in [3,7]:
            empty = 2
        else:
            empty = 0 
    else:
        empty = (n*m)%2 
        
    print(n*m) - empty 
    