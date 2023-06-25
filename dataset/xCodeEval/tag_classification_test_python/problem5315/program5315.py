    from sys import path_hooks, stdin, stdout
    import sys
    
     
def mapinput():
        return  map(int, stdin.readline().split())
    
    
    n , m  = mapinput()
    
    factors = [ [] for i in range(n+1) ] 
    for i in range( 1, n+1 ):
        for j in range( i+i  , n +1 , i ):
            factors[j].append(i)
    
    for test in range(1):
    def solve():
            memo = {0:0 , 1:1 , 2:2 , 3: 5}
            for i in range(4 , n+1):
                ans = memo[i-1] * 2
                for j in factors[i]:
                    ans += memo[j] - memo[j-1]
                ans %= m
                memo[i] = ans
            return memo[n]
    
    
    
        print(solve())
    