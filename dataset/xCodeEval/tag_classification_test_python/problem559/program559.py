    n = int(input())
    
def fact(n):
        f = i = 1
        while i <= n:
            f *= i
            i += 1
        return f
    
    print((fact(n)) * fact(n)) / (fact(n - 5) * fact(n - 5) * fact(5))