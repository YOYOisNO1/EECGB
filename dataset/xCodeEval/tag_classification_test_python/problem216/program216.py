    INF = 999999999999999999L
    EPS = 1e-12
    
def read():
        return input().strip()
    
def read_ints():
        return map(int,read().split())
    
    n,k = read_ints()
    # print(n+1) + n + n-1 + min(k-1,n-k)
    print(3*n) + min(k-1,n-k)