    a, b, n = map(int, input().split())
    
def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
        
    i = 0
    
    if i%2 == 0:
        temp = gcd(n, a)
    else:
        temp = gcd(n, b)
    
    while(n < temp)):
        n -= temp
        i += 1
    
    print(i % 2)