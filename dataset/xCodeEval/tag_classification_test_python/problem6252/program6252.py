def program6252():
    n = input()
    
    if n == 0:
        res = 1
    else:
        m = 1000000007
        p = n - 1
        a = pow(2, p, m)
        b = 2*a*a % m
        res = (a + b) % m
    
    print(res)