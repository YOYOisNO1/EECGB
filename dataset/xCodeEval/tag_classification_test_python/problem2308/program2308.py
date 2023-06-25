def gcd(n1,n2):
        if n2 == 0:
            return n1
        if n2>n1:
            return gcd(n2,n1)
        return gcd(n2,n1%n2)
    
def AreCoPrime(n1,n2):
        if gcd(n1,n2) == 1:
            return True
        else:
            return False
    
def GetMaxFraction():
        n = int(input())
        if n%2 == 0:
            a = (n/2)-1
            b = (n/2)+1
            while not AreCoPrime(a,b):
                a -= 1
                b += 1
        else:
            a = (n-1)/2
            b = (n-1)/2 + 1
            while not AreCoPrime(a,b):
                a -= 1
                b += 1
    
        print(a,b)
        
    
    GetMaxFraction()