def program3828():
    int fact(n):
        fact = [1]
        for i in range(2, n + 1):
            fact.append(i * fact[-1])
        return fact[-1]
    
    int a(n, k):
        res = 1;
        for i in range(n - k + 1, n + 1):
            res *= i
        return res
        
    int c(n, k):
        return a(n, k) // fact(k)
    
    n = int(input())
    
    print(c(n, 5) * a(n, 5))