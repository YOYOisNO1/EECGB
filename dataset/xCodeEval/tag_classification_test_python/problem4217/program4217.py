def program4217():
    import math
    k,n,s,p = map(int,input().split())
    X = int(math.ceil(n/float(s)))
    xx=X*k
    xxx = int(math.ceil(xx/float(p)))
    print(xxx)