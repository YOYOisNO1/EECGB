def dp(n):
        if n == 0:
            return 0
        if n % 2 == 1:
            return 0
        
        return 2**(n//2)
        
        
    n = int(input())
    print(dp(n))