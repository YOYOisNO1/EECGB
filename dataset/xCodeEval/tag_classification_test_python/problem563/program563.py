def silnia(n):               
        if n == 0:
            return 1
        else:
            return n * silnia(n-1)
    x=input()
    print((silnia(x)/(120*silnia(x-5)))*x*(x-1)*(x-2)*(x-3)*(x-4))