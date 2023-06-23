def fact(n):
        if n==1:
            return 1
        return fact(n-1)*n%(10**9+7)
        
def rev(a):
        return pow(a,10**9+5,10**9+7)
    
def c2nn(n):
        return fact(2*n)*rev(fact(n)**2)%(10**9+7)
    
    n=int(input())
    print(c2nn(n)*2-n)