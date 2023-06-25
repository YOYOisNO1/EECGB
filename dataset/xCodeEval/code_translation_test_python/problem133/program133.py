def program133():
    X = (input())
    n = len(X)
    x = int(X,2)
    print(((2**(n-1))*(x))%1000000007)