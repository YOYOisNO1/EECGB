    
def isprime(n):
        if n <= 1: return False
        if n == 2: return True
        if n % 2 == 0: return False
    
        x = 3
        while x*x <= n:
            if n % x == 0: return False
            x += 2
        return True
    
def calc(n, m):
        x = n+1
        while x <= m:
            if isprime(x):
                return x == m
            x += 1
        return False
    
def main():
        n, m = map(int, input().split())
    
        if calc(n, m):
            print("YES")
        else:
            print("NO")
    
    main()
    
    
        
        