    t = int(input())
    
    import math
    
def lcm(a,b):
        return (a*b)//math.gcd(a,b)
    
def isPrime(n) : 
        if (n <= 1) : 
            return False
        if (n <= 3) : 
            return True
        if (n % 2 == 0 or n % 3 == 0) : 
            return False
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                return False
            i = i + 6
      
        return True
    
    for k in range(t):
        n = int(input())
        if n%2 == 0:
            print(f'{n//2} {n//2}')
        elif isPrime(n):
            print(f'{1} {n-1}')
        else:
            x = math.inf
            for i in range(3,int(math.sqrt(n))+1,1):
                if n%i == 0:
                    x = min(x,i)
            ansX = n//x
            print(f'{ansX} {n - ansX}')
    
    
    
        