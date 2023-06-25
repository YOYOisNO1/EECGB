    n = input()
    
    if n == 1:
        print(0)
        exit()
    
def f(n):
        if n == 1: return 1
        
        q = 1
        k = 0
        while q < n:
            q <<= 1
            k += 1
        if q > n:
            q >>= 1
            k -= 1
            
        if n == q: return (q // 2) * (k + 2)         
        
        return ((q // 2) * (k + 2) + f(n - q)) 
    
    print(f(n) - 1)   