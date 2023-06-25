    import math
    
def calculateFactorial(z):
        result = 1
        for i in range(1, z+1):
            result *= i
        return result
    
def calculateBinomial(n, k):
        return calculateFactorial(n)/(calculateFactorial(k)*calculateFactorial(n-k))
    
    n = int(input())
    ans = 2*calculateFactorial(n)/n**2
    print(int(ans))