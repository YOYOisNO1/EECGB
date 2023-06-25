def program211():
    n = long(input())
    i = 2
    while i * i <= n:
        if n % i == 0:
            print(n / i)
            exit(0)
        i += 1
    
    print(1)