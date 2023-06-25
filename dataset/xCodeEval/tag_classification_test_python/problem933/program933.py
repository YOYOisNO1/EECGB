    INF = 999999999999999999L
    EPS = 1e-12
    
def read():
        return input().strip()
    
def read_ints():
        return map(int,read().split())
    
    n,a,b = read_ints()
    a -= 1 
    b -= 1
    c = a^b 
    round = 0
    while c > 0:
        c >>= 1 
        round += 1
    if (1<<round) == n:
        print("Final!")
    else:
        print(round) 