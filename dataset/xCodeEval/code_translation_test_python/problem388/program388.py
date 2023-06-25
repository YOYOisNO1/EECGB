    
    
    n,k = map(int, input().split())
    
    m=10**k
    
def gcd(a,b):
        if a<b:
            a,b=b,a
        while b>0:
            a,b=b,a%b
        return a
    
    print(m*n/gcd(m,n))
    
    