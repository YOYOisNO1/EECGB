def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
def coprime(a, b):
        return gcd(a, b) == 1
    n=input()
    a=n/2
    b=n-(n/2)
    while coprime(a,b)==False:
    	a=a-1
    	b=b+1
    print(a,b)